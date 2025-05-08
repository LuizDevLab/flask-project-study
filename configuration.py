from routes.home import home_route
from routes.cliente import cliente_route

def configure_all(app):
  configure_routes(app)


def configure_routes(app):
  app.register_blueprint(home_route) 
  app.register_blueprint(cliente_route, url_prefix='/clientes')


def configure_db():
  pass