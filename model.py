from google.appengine.api import quota
from google.appengine.ext import db
import random


class RequestRecord(db.Model):
  method = db.StringProperty(required=True)
  path = db.StringProperty(required=True)
  request_headers = db.StringListProperty(required=True)
  status_code = db.IntegerProperty(required=True)
  status_text = db.StringProperty(required=True)
  response_headers = db.StringListProperty(required=True)
  wall_time = db.IntegerProperty(required=True)
  api_time = db.IntegerProperty(required=True)
  random = db.FloatProperty(required=True)

  @classmethod
  def create(cls, request, response, elapsed):
    status_code, status_text = response.status.split(' ', 1)
    return cls(
        method=request.method,
        path=request.path_qs,
        request_headers=['%s: %s' % x for x in request.headers.items()],
        status_code=status_code,
        status_text=status_text,
        response_headers=['%s: %s' % x for x in response.headers.items()],
        wall_time=elapsed,
        api_time=quota.get_request_cpu_usage(),
        random=random.random())
