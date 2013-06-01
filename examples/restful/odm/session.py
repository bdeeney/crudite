from ming.datastore import DataStore
from ming.odm import ThreadLocalORMSession

__all__ = ['session']

engine = DataStore(database='flask_tutorial')
session = ThreadLocalORMSession(bind=engine)
