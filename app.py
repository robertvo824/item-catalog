from flask import Flask, render_template, request
from flask import redirect, url_for, flash, jsonify
from sqlalchemy import create_engine, desc, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets, FlowExchangeError
from oauth2client.client import AccessTokenCredentials
import httplib2
import json
from flask import make_response
import requests
from functools import wraps
import helperFunctions

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in login_session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function


app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Login route, create anit-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(
        random.choice(
            string.ascii_uppercase +
            string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('show_login.html', STATE=state)

# CONNECT - Google login get token


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data.decode('utf-8')

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = (
        'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' %
        access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    # check to see if user is already logged in
    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')

    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # return credential object
    credentials = AccessTokenCredentials(
        login_session['credentials'], 'user-agent-value')

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['image'] = data['picture']
    login_session['email'] = data['email']

    # see if user exists, if it doesn't make a new one
    user_id = helperFunctions.get_user_id(login_session['email'])
    if not user_id:
        user_id = helperFunctions.create_user(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['image']
    output += """ " style = "width: 300px; height: 300px;border-radius: 150px;
    -webkit-border-radius: 150px;
    -moz-border-radius: 150px;">"""
    flash("You are now logged in as %s" % login_session['username'])
    print("done!")
    return output

# DISCONNECT - Revoke a current user's token and reset their login_session


@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    credentials = AccessTokenCredentials(
        login_session['credentials'], 'user-agent-value')

    if credentials is None:
        response = make_response(json.dumps('Current user not '
                                            'connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    access_token = credentials.access_token
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    reason = h.request(url, 'GET')[1]
    if result['status'] == '200':
        # Reset the user's sesson.
        del login_session['credentials']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['image']

        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        flash("You have successfully logged out.")
        return redirect(url_for('show_homepage'))
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(json.dumps('Failed to revoke token for given '
                                            'user. reason: '
                                            '{reason}'.format(reason=reason),
                                            400))
        response.headers['Content-Type'] = 'application/json'
        return response

# RESTful ROUTES


@app.route('/')
def show_homepage():
    items = session.query(Item).order_by(Item.id.desc()).limit(5).all()
    return render_template("index.html", items=items)


# CRUD ROUTES

@app.route('/<category_id>/')
def categoryVinyls(category_id):
    category = session.query(Category).filter_by(id=category_id).first()
    items = session.query(Item).filter_by(
        category_id=category_id).order_by(
        Item.id.desc())
    return render_template("show_cat.html", category=category, items=items)


@app.route('/catalog/myvinyls/')
def showMyVinyls():
    """If logged in, show the user the items they have added."""
    if 'username' not in login_session:
        return redirect('/login')
    category = session.query(Category).filter_by(id=7).first()
    user_id = helperFunctions.get_user_id(login_session['email'])
    items = session.query(Item).filter_by(
        user_id=login_session['user_id']).all()

    if not items:
        flash("Your collection is empty!")

    return render_template('my_vinyls.html', items=items, category=category)


# new vinyl/item route and function
@app.route("/<category_id>/new/", methods=["GET", "POST"])
@login_required
def newItem(category_id):
    if request.method == "POST":
        newItem = Item(artist=request.form["artist"],
                       album=request.form['album'],
                       year=request.form['year'],
                       image=request.form['image'],
                       description=request.form['description'],
                       category_id=category_id,
                       user_id=login_session['user_id'])
        session.add(newItem)
        session.commit()
        flash(request.form["artist"] + " vinyl added!")
        return redirect(url_for("categoryVinyls", category_id=category_id))
    else:
        return render_template("new_item.html", category_id=category_id)

# Route to show item


@app.route("/<category_id>/<item_id>/")
def showItem(category_id, item_id):
    foundItem = session.query(Item).filter_by(
        id=item_id, category_id=category_id).one()
    return render_template('show_item.html', item=foundItem)


# Route for editing vinyl/item


@app.route("/<category_id>/<item_id>/edit", methods=["GET", "POST"])
@login_required
def editItem(category_id, item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    if item.user_id != login_session['user_id']:
        flash("You are not authorized to edit this vinyl!")
        return redirect(url_for('categoryVinyls', category_id=category_id))
    if request.method == 'POST':
        if request.form['artist']:
            item.artist = request.form['artist']
        if request.form['album']:
            item.album = request.form['album']
        if request.form['year']:
            item.year = request.form['year']
        if request.form['image']:
            item.image = request.form['image']
        if request.form['description']:
            item.description = request.form['description']
        session.add(item)
        session.commit()
        flash("Vinyl has been edited")
        return redirect(url_for('categoryVinyls', category_id=category_id))
    else:
        # USE THE RENDER_TEMPLATE FUNCTION BELOW TO SEE THE VARIABLES YOU
        # SHOULD USE IN YOUR EDITMENUITEM TEMPLATE
        return render_template(
            'edit_item.html',
            category_id=category_id,
            item_id=item_id,
            item=item)


# Delete an item.
@app.route("/<category_id>/<item_id>/delete", methods=["GET", "POST"])
@login_required
def deleteItem(category_id, item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    if item.user_id != login_session['user_id']:
        flash("You are not authorized to delete this vinyl!")
        return redirect(
            url_for(
                'categoryVinyls',
                category_id=item.category_id))
    if request.method == "POST":
        session.delete(item)
        session.commit()
        flash("Vinyl has been deleted")
        return redirect(
            url_for(
                'categoryVinyls',
                category_id=item.category_id))
    else:
        return render_template('delete_item.html', item=item)


# JSON endpoint for the whole catalog.
@app.route('/catalog.json')
def show_all_items_json():
    items = (
        session.query(Item)
        .order_by(Item.category_id)
        .order_by(Item.artist)
        .all()
    )
    return jsonify(Items=[i.serialize for i in items])


# JSON endpoint for a category.
@app.route('/<category_id>.json')
def show_items_json(category_id):
    items = session.query(Item).filter_by(
        id=category_id).order_by(
        Item.artist).all()
    return jsonify(Items=[i.serialize for i in items])


# JSON endpoint for an item.
@app.route('/<category_id>/<item_id>.json')
def show_item_json(category_id, item_id):
    item = session.query(Item).filter_by(id=item_id).first()
    return jsonify(Item=item.serialize)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
