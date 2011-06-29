def webapp_add_wsgi_middleware(app):
  from clio import middleware
  return middleware.LoggingMiddleware(app)
