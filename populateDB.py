from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item
from sqlalchemy.pool import SingletonThreadPool

engine = create_engine('sqlite:///catalog.db', poolclass=SingletonThreadPool)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Vinyls for Classic Rock
category1 = Category(name="Classic Rock")

session.add(category1)
session.commit()

item1 = Item(
    artist="Bob Dylan",
    album="The Freewheelin' Bob Dylan",
    description="""Freewheelin' is the first Dylan album where you
    can tell he was going to be someone incredible.""",
    image="""https://img.discogs.com/AdwZbbhZhVGbGrolI5i8s_PotNU=
/fit in600x589/filters:strip_icc():
format(jpeg):mode_rgb():quality(90)/
discogs-images/R-2057737-1261406197.jpeg.jpg""",
    year=1963,
    category=category1)

session.add(item1)
session.commit()

item2 = Item(
    artist="Pink Floyd",
    album="The Wall",
    description="""The Wall is one of the greatest
    concept albums of all time.""",
    image="""https://img.discogs.com/3wslOvgfkuqMpxN9ljKGFBDpjUY=
/fit-in/300x300/filters:strip_icc():format(jpeg):
mode_rgb():quality(40)/discogs-images/R-367511-
1529077021-1155.jpeg.jpg""",
    year=1979,
    category=category1)

session.add(item2)
session.commit()

item3 = Item(
    artist="The Rolling Stones",
    album="Exile On Main St.",
    description="""Listening to Exile on Main St. hardly
    creates a sense of highly-crafted musicianship
    or fine-tuned production.""",
    image="""https://cdn.pastemagazine.com/www/blogs/
lists/assets_c/2012/05/220px-ExileMainSt-thumb-
250x250-67371.jpg""",
    year=1972,
    category=category1)

session.add(item3)
session.commit()

item4 = Item(
    artist="Aerosmith",
    album="Aerosmith",
    description="""Aerosmith is the eponymous debut studio
    album by American rock band Aerosmith, released
    on January 5, 1973 by Columbia Records.The song
    \"Walkin' the Dog\" is a cover of a song originally
    performed by Rufus Thomas. The single \"Dream On\"
    became an American top ten single when
    re-released in 1976.""",
    image="""https://upload.wikimedia.org/wikipedia/en/
thumb/5/58/Aerosmith_-_Aerosmith.jpg/
220px-Aerosmith_-_Aerosmith.jpg""",
    year=1973,
    category=category1)

session.add(item4)
session.commit()

# Vinyls for Blues
category1 = Category(name="Blues")

session.add(category1)
session.commit()

item1 = Item(
    artist="B.B. King",
    album="Live At The Regal",
    description="""The album is considered one of
    the greatest blues recordings ever.""",
    image="""https://images-na.ssl-images-
amazon.com/images/I/61zDQ-Fv8QL._SY355_.jpg""",
    year=1964,
    category=category1)

session.add(item1)
session.commit()

item2 = Item(
    artist="Eric Clapton",
    album="Unplugged",
    description="""Eric Clapton's Unplugged was responsible
    for making acoustic-based music, and 'unplugged'
    albums in particular, a hot trend in the early 90s.""",
    image="""https://images-na.ssl-images-amazon.com/
images/I/71-O7VtV3xL._SY355_.jpg""",
    year=2011,
    category=category1)

session.add(item2)
session.commit()

item3 = Item(
    artist="Jimi Hendrix",
    album="Blues",
    description="""While Hendrix remains most famous for his hard
    rock and psychedelic innovations, more than a third of his
    recordings were blues-oriented. These two records contain 11
    blues originals and covers, eight of which were
    previously unreleased. Recorded from 1966-70, they
    feature the master guitarist stretching the
    boundaries of electric blues in both live
    and studio settings.""",
    image="""https://images-na.ssl-images-
amazon.com/images/I/51WjEEgbWjL._SX355_.jpg""",
    year=1994,
    category=category1)

session.add(item3)
session.commit()

# Vinyls for Hard Rock
category1 = Category(name="Hard Rock")

session.add(category1)
session.commit()


item1 = Item(
    artist="Def Leppard",
    album="Hysteria",
    description="""Hysteria is the fourth studio album by English
    hard rock band Def Leppard.""",
    image="""https://images-na.ssl-images-amazon.com/
images/I/61m1lCCsLTL._AC_US218_.jpg""",
    year=1987,
    category=category1)

session.add(item1)
session.commit()

item2 = Item(
    artist="AC/DC",
    album="Back in Black",
    description="""Back in Black is the seventh studio album by
    Australian rock band AC/DC.""",
    image="""https://images-na.ssl-images-amazon.com/
images/I/51QBqqMxyoL._SY355_.jpg""",
    year=2003,
    category=category1)

session.add(item2)
session.commit()

item3 = Item(
    artist="Metallica",
    album="Master Of Puppets",
    description="""The album has been certified 6x Platinum
    in the United States and has sold over 10 million
    copies worldwide.""",
    image="""https://images-na.ssl-images-amazon.com/
images/I/81hryXAVZjL._SY355_.jpg""",
    year=1972,
    category=category1)

session.add(item3)
session.commit()

item4 = Item(
    artist="Linkin Park",
    album="Meteora",
    description="""Meteora is the second studio album
    by American rock band Linkin Park. It was released
    on March 25, 2003 through Warner Bros. Records,
    following Reanimation, a collaboration album
    which featured remixes of songs included
    on their 2000 debut studio album Hybrid Theory.""",
    image="""https://cdn.shopify.com/s/files/1/2117/
2713/products/LIP-81-B009_grande.jpg?v=
1507572319""",
    year=2003,
    category=category1)

session.add(item4)
session.commit()

# Vinyls for Pop
category1 = Category(name="Pop")

session.add(category1)
session.commit()


item1 = Item(
    artist="Michael Jackson",
    album="Thriller",
    description="""Two vinyl LP pressing of the 25th anniversary
    edition of Michael Jackson's Thriller celebrates the groundbreaking
    album with eight bonus tracks, five of them previously unreleased.
    The new tracks include remixes from Kanye West, Akon, and will.i.am,
    as well as 'For All Time', a previously unreleased track from the
    Thriller sessions that has been newly mixed and mastered by Michael
    Jackson.""",
    image="""https://images-na.ssl-images-amazon.com/
images/I/81m2C4XYjML._SY355_.jpg""",
    year=2008,
    category=category1)

session.add(item1)
session.commit()

item2 = Item(
    artist="Madonna",
    album="Madonna",
    description="""Vinyl reissue of this 1983 album from the
    award-winning, multi-platinum selling, trend-setting Pop/Dance
    diva. Features \"Lucky Star,\" \"Holiday,\" \"Borderline\"
    and many more.""",
    image="""https://images-na.ssl-images-amazon.com/
images/I/81iEFzaJEvL._SY355_.jpg""",
    year=2016,
    category=category1)

session.add(item2)
session.commit()

item3 = Item(
    artist="Justin Timberlake",
    album="The 20/20 Experience",
    description="""Double vinyl LP pressing. 2013 release, the
    third solo album from the Grammy and Emmy winning Pop
    superstar, actor and former member of NSync. The 20/20
    Experience is the long-awaited follow-up to his album
    FutureSex/LoveSounds (2006).""",
    image="""https://images-na.ssl-images-amazon.com/
images/I/81-6ucaI5%2BL._SY355_.jpg""",
    year=2013,
    category=category1)

session.add(item3)
session.commit()

item4 = Item(
    artist="Jackson 5",
    album="ABC",
    description="""ABC was the second studio album by The Jackson 5,
    issued on May 8, 1970 on Motown Records. It featured the
    number-one singles 'ABC' and 'The Love You Save'.""",
    image="""https://images-na.ssl-images-amazon.com
/images/I/71cBrakTspL._SY355_.jpg""",
    year=1970,
    category=category1)

session.add(item4)
session.commit()


# Vinyls for Country
category1 = Category(name="Country")

session.add(category1)
session.commit()


item1 = Item(
    artist="Willie Nelson",
    album="Red Headed Stranger",
    description="""Willie's 1975 concept album, with its mystic
    and religious overtones, broke all of the traditional rules
    of Country music and helped establish Austin, Texas as
    ground zero of the \"Outlaw\" movement!""",
    image="""https://images-na.ssl-images-amazon.com
/images/I/51JINvLCNUL._SY355_.jpg""",
    year=1975,
    category=category1)

session.add(item1)
session.commit()

item2 = Item(
    artist="Dierks Bentley",
    album="Black",
    description="""Black is personal - after all, it's named after
    his wife Cassidy s maiden name, but it's really a record about
    the human heart not any particular human. It explores breakups,
    hookups, mess-ups and everything inbetween, shining a light
    on the things that happen after the sun goes down.""",
    image="""https://images-na.ssl-images-amazon.com
/images/I/919Bwo5cWZL._SY355_.jpg""",
    year=2016,
    category=category1)

session.add(item2)
session.commit()

item3 = Item(
    artist="Johnny Cash",
    album="American IV: The Man Comes Around",
    description="""Limited vinyl LP pressing of this 2002 album
    from the Country legend. This is the last album released
    before his death in 2003. The majority of songs are covers
    which Cash performs in his own spare style, with help from
    producer Rick Rubin.""",
    image="""https://images-na.ssl-images-amazon.com
/images/I/71D%2BRcm7-XL._SY355_.jpg""",
    year=2014,
    category=category1)

session.add(item3)
session.commit()

item4 = Item(
    artist="Eric Church",
    album="Sinners Like Me",
    description="""This is Eric Church s debut certified GOLD
    album which was released in 2006. The album includes the Top
    hits How Bout Me, Two Pink Lines, Guys Like Me, and Sinners
    Like Me . This Vinyl will be on 180 Gram RED Vinyl and will
    be released on January 25th.""",
    image="""https://images-na.ssl-images-amazon.com
/images/I/81Km5iT1kPL._SY355_.jpg""",
    year=2006,
    category=category1)

session.add(item4)
session.commit()

# Vinyls for Soundtracks
category1 = Category(name="Soundtracks")

session.add(category1)
session.commit()


item1 = Item(
    artist="Grease",
    album="The Original Soundtrack from The Motion Picture",
    description="""The movie is a 1970s take on 1950s musicals,
    providing all the kitsch anyone could hope for. It's John Travolta
    as Danny Zuko as Olivia Newton-John's pompadoured main squeeze,
    and the kids go crazy.""",
    image="""https://img.discogs.com/Cb_no86c5rOQVBaivUb5ngPginQ=
/fit-in/300x300/filters:strip_icc():format(jpeg):mode_rgb():
quality(40)/discogs-images/R-631742-1168562192.jpeg.jpg""",
    year=1978,
    category=category1)

session.add(item1)
session.commit()

item2 = Item(
    artist="Dirty Dancing",
    album="Original Motion Picture Soundtrack",
    description="""Have the time of your life with the unforgettable
    soundtrack to Dirty Dancing!""",
    image="""https://images-na.ssl-images-amazon.com
/images/I/71SHjN7c%2BCL._SY355_.jpg""",
    year=2015,
    category=category1)

session.add(item2)
session.commit()

item3 = Item(
    artist="The Greatest Showman",
    album="Original Motion Picture Soundtrack",
    description="""The Greatest Showman: Original Motion Picture
    Soundtrack is the soundtrack album to the film The Greatest
    Showman. It was released in full on December 8, 2017 by Atlantic
    Records.""",
    image="""https://images-na.ssl-images-amazon.com
/images/I/81-05GNqsdL._SY355_.jpg""",
    year=2017,
    category=category1)

session.add(item3)
session.commit()

# Vinyls for My Vinyls
category1 = Category(name="My Vinyls")

session.add(category1)
session.commit()

print("Add vinyl items!")
