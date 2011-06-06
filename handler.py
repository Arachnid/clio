from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from config import config


application = webapp.WSGIApplication([
])


def main():
  run_wsgi_app(application)


if __name__ == "__main__":
  main()
