import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app


class PageHandler(webapp.RequestHandler):
  """Renders a generic page that describes its own parameters."""

  def post(self):
    self.handle_request()

  def get(self):
    self.handle_request()

  def handle_request(self):
    template_path = os.path.join(os.path.dirname(__file__), 'page.html')
    self.response.out.write(template.render(template_path, {
        'request': self.request,
        'response': self.response,
    }))


application = webapp.WSGIApplication([
    ('/.*', PageHandler),
], debug=True)


def main():
  run_wsgi_app(application)


if __name__ == '__main__':
  main()
