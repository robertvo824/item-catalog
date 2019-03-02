# Project : Item Catalog
### by Robert Vo
Item Catalog project, part of the Udacity [Full Stack Web Developer
Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Project Description
This app runs a website that shows a collection of vinyl records. The records are organized into genres and the user can log in with Google credentials to add to a personal collection.

## Requirements
The project code requires the following software:

* Python 2.7.x
* [SQLAlchemy](http://www.sqlalchemy.org/) 0.8.4 or higher (a Python SQL toolkit)
* [Flask](http://flask.pocoo.org/) 0.10.1 or higher (a web development microframework)
* The following Python packages:
    * oauth2client
    * requests
    * httplib2


You can run the project in a Vagrant managed virtual machine (VM) which includes all the required dependencies (see below for how to run the VM).

For this you will need [Vagrant](https://www.vagrantup.com/downloads) and
[VirtualBox](https://www.virtualbox.org/wiki/Downloads) software installed on your system. Instructions are below.

## Project Contents
This project consists for the following files in the `item-catalog` directory:

* `app.py` - The main Python script that serves the website.
* `client_secrets.json` - Client secrets for Google OAuth login.
* `README.md` - This read me file.
* `/templates` - Directory containing the HTML templates for the website, using the [Jinja 2](http://jinja.pocoo.org/docs/dev/) templating language for Python.
* `database_setup.py` - Defines the database classes and creates an empty database.
* `populate_database.py` - Inserts a selection of vinyls into the database.
* `helperFunctions.py` - Includes functions for checking and creating users.

### Templates
The `/templates` directory contains the following files, written in HTML and the Jinja2
templating language:

* `delete_item.html` - Delete vinyl.
* `edit_item.html` - Form to edit the details of a vinyl.
* `index.html` - The default page that shows most recents vinyls.
* `show_item.html` - A page that displays a single vinyl and details.
* `show_cat.html` - A page that lists the vinyls belonging to a single category.
* `main.html` - This defines the common layout of the website and is the parent for all the other template pages.
* `show_login.html` - A login page featuring OAuth Google login button.
* `my_vinyls.html` - A page for displaying the vinyls you have added to the website.
* `new_item.html` - A form for adding a new vinyl.

## Get the Project
Download the project zip file to you computer and unzip the file. Or clone this repository to your desktop.

Open the text-based interface for your operating system (e.g. the terminal
window in Linux, the command prompt in Windows).

Navigate to the project directory and then enter the `vagrant` directory.

### Start VM
Bring up the VM with the following command:

```bash
vagrant up
```

The first time you run this command it will take awhile, as the VM image needs to be downloaded.

You can then log into the VM with the following command:

```bash
vagrant ssh
```

More detailed instructions for installing the Vagrant VM can be found
[here](https://www.udacity.com/wiki/ud197/install-vagrant).

### Update versions of Flask

```bash
sudo pip install werkzeug==0.8.3
sudo pip install flask==0.9
sudo pip install Flask-Login==0.1.3
```

### Navigate to the item-catalog directory with this command:

```bash
cd /vagrant/item-catalog
```

### OAuth setup
In order to log in to the web app, you will need to get either a Google OAuth app ID and secret. For Google, go to the
[Google Developers Console](https://console.developers.google.com/).

Once you have your credentials, put the IDs and secrets in the `client_secrets.json` for file Google.

You will now be able to log in to the app.

### Run database_setup.py

```bash
python database_setup.py
```

### Run populateDB.py

```bash
python populateDB

```### Run app.py

```bash
python app.py
```

It then starts a web server that serves the application. To view the application,
go to the following address using a browser on the host system:

```
http://localhost:5000/
```

You should see over a dozen vinyls that were seeded to the database. Implemented Google login because I didn't want to create a Facebook account. You can browse the populated vinyls, but cannot edit or delete them. In order to add vinyls to a personal collection, login with your Google credentials. You can also view the json endpoints without loggin in.


### Shutting the VM down
When you are finished with the VM, press `Ctrl-D` to logout of it and shut it down
with this command:

```bash
vagrant halt
```

## Miscellaneous
This README document is based on a template suggested by PhilipCoach in this
Udacity forum [post](https://discussions.udacity.com/t/readme-files-in-project-1/23524).
