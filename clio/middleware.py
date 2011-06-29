import random
import time
import webob

from google.appengine.api import prospective_search
from google.appengine.api import quota

from clio.config import config
from clio import model


def _stringifyHeaders(header_dict):
  return ['%s: %s' % x for x in header_dict.items()]


class LoggingMiddleware(object):
  def __init__(self, application):
    self.application = application

  def __call__(self, environ, start_response):
    # Don't record if the request is to clio itself, or the config says no.
    if (environ['PATH_INFO'] == config.QUEUE_URL or
        environ['PATH_INFO'].startswith(config.BASE_URL) or
        not config.should_record(environ)):
      return self.application(environ, start_response)

    request = webob.Request(environ)
    start_time = time.time()
    response = request.get_response(self.application)
    elapsed = int((time.time() - start_time) * 1000)
    status_code, status_text = response.status.split(' ', 1)

    record = model.RequestRecord(
        method=request.method,
        path=request.path_qs,
        request_headers=_stringifyHeaders(request.headers),
        status_code=int(status_code),
        status_text=status_text,
        response_headers=_stringifyHeaders(response.headers),
        wall_time=elapsed,
        cpu_time=quota.get_request_cpu_usage(),
        random=random.random())
    prospective_search.match(
        record,
        result_relative_url=config.QUEUE_URL,
        result_task_queue=config.QUEUE_NAME)
    return response(environ, start_response)
