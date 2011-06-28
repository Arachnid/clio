import random
import time
import webob

from google.appengine.api import prospective_search
from google.appengine.api import quota

from config import config
import model


def _stringifyHeaders(header_dict):
  return ['%s: %s' % x for x in header_dict.items()]


class LoggingMiddleware(object):
  def __init__(self, application):
    self.application = application

  def __call__(self, environ, start_response):
    req = Request(environ)
    start_time = time.time()
    resp = req.get_response(self.application)
    elapsed = time.time() - start_time
    status_code, status_text = response.status.split(' ', 1)
    if config.config.should_record(env):
      record = model.RequestRecord(
          method=request.method,
          path=request.path_qs,
          request_headers=_stringifyHeaders(request.headers)
          status_code=status_code,
          status_text=status_text,
          response_headers=_stringifyHeaders(response.headers),
          wall_time=elapsed,
          cpu_time=quota.get_request_cpu_usage(),
          random=random.random())
      prospective_search.match(record, config.QUEUE_URL, config.QUEUE_NAME)
    return resp(environ, start_response)
