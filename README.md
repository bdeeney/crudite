# Crudité #

Crudité is a Flask-powered framework for creating RESTful web services that
expose CRUD-style models as collection-entry resource pairs.

## Prerequisites ##

Install and configure Python 2.7 and related utilities:

    sudo port install python27 py27-pip mongodb
    sudo port select python python27
    sudo ln -fs /opt/local/bin/pip-2.7 /opt/local/bin/pip
    echo /opt/local/Library/Frameworks/Python.framework/Versions/2.7/bin \
        | sudo tee /etc/paths.d/macports.python > /dev/null
    source /etc/zshenv
    sudo easy_install -a readline
    sudo pip install --upgrade virtualenv

To run the examples, a MongoDB server is required:

    sudo port install mongodb
    sudo launchctl load -w /Library/LaunchDaemons/org.macports.mongodb.plist

## Installation ##

To install Crudité from source:

    git clone git@github.colo.lair:bryand/crudite.git
    cd crudite
    make test

## Development Environment - Recommended Enhancements ##

IPython and the rednose nose plugin are highly recommended for any Python
development environment.  To install these tools in the Crudité virtualenv:

    . env/bin/activate
    pip install ipython rednose
