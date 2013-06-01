from flask import Flask

from crudite import Crudite


class DescribeCrudite(object):

    def should_subclass_flask(self):
        assert issubclass(Crudite, Flask)
