from pprint import pprint

from restful.model import User, Message, Template
from restful.odm import init_db
from restful.odm.session import session

# drop MongoDB database
session.impl.bind.conn.drop_database(session.impl.db.name)
init_db(session)

# preload some users
alice = User(username='alice', email='alice@example.com', first_name='Alice')
bob = User(username='bob', email='bsmith@example.com',
           first_name='Bob', last_name='Smith')
charlie = User(username='cbrown', email='cbrown@example.com',
               first_name='Charles', last_name='Brown', is_active=False)

# preload some templates
ski = Template(name='Ski Adventure', html='<html>Winter Getaway</html>')
vegas = Template(name='Vegas', plaintext='Win Big!',
                 html='<html>Win Big!</html>')

session.flush()

# preload some messages
specials = Message(subject="Alice's Restaurant Specials", user=alice,
                   template=vegas, html='<html>Our Weekly Specials...</html>')
concerts = Message(subject="Live Music @ Alice's Restaurant", user=alice,
                   html='<html>Every Friday night...</html>')
deals = Message(subject='Last-minute Weekend Travel Deals', user=bob,
                template=ski, html='<html>Book now...</html>')

session.flush()

for model in [User, Message, Template]:
    print '-' * 70
    collection = model.__mongometa__.name
    total = model.query.find().count()
    print '{0} ({1}):'.format(collection, total)
    pprint(model.query.find().all(), indent=2, depth=10)
    print '-' * 70 + '\n'
