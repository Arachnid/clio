from google.appengine.ext import db


class RequestRecord(db.Model):
  """Encapsulates information for a request log record."""

  method = db.StringProperty(required=True)
  path = db.StringProperty(required=True)
  request_headers = db.StringListProperty(required=True)
  status_code = db.IntegerProperty(required=True)
  status_text = db.StringProperty(required=True)
  response_headers = db.StringListProperty(required=True)
  wall_time = db.IntegerProperty(required=True)
  cpu_time = db.IntegerProperty(required=True)
  random = db.FloatProperty(required=True)

  def to_json(self):
    """Returns a dict containing the relevant information from this record.
    
    Note that the return value is not a JSON string, but rather a dict that can
    be passed to a JSON library for encoding."""
    return dict((k, v.__get__(self, self.__class__))
                for k, v in self.properties().iteritems())


class Subscription(db.Model):
  """Provides information on a client subscription to a filtered log feed."""

  client_id = db.StringProperty(required=True)
  created = db.DateTimeProperty(required=True, auto_now=True)
  expires = db.DateTimeProperty(required=True)
