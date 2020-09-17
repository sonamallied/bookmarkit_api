import os

# You need to replace the next values with the appropriate values for your configuration

basedir = os.path.abspath(os.path.dirname(__file__))

#class Config(object):
DEBUG = False
TESTING = False
SECRET_KEY = 'this-really-needs-to-be-changed'
MONGODB_HOST = 'mongodb://localhost:27017/bookmarkit'

