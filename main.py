from flask import Flask
from routes.home import home_route

#inicialização
app = Flask(__name__)

app.register_blueprint(home_route) 

# execucao
app.run(debug=True)