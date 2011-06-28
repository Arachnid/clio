import datetime

from google.appengine.api import lib_config


class ConfigDefaults(object):
  """Configurable constants.
  
  To override clio's configuration values, define values like this in your
  appengine_config.py file (in the root of your app):
  
    clio_FOO = 5
  """
  BASE_URL = '/_clio'
  QUEUE_URL = '/_clio/match'
  QUEUE_NAME = 'default'
  SUBSCRIPTION_TIMEOUT = datetime.timedelta(hours=2)


config = lib_config.register('clio', ConfigDefaults.__dict__)
