from os.path import devnull, dirname, join
from subprocess import Popen


def load(url, delay='0'):
    """Load/reload the specified URL in a browser."""
    Popen([join(dirname(__file__), 'load.scpt'), url, delay],
          stdout=open(devnull))
