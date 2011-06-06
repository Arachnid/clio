import time
import webob

from google.appengine.api import prospective_search

from config import config
import model


class LoggingMiddleware(object):
  def __init__(self, application):
    self.application = application

  def __call__(self, environ, start_response):
    req = Request(environ)
    start_time = time.time()
    resp = req.get_response(self.application)
    elapsed = time.time() - start_time
    if config.config.should_record(env):
      record = model.RequestRecord.create(request, response, elapsed)
      prospective_search.match(record, config.QUEUE_URL, config.QUEUE_NAME)
    return resp(environ, start_response)
