from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database\\application.db'
db = SQLAlchemy(app)

api = Api(app)

from myapp.jogador.views import jogador
app.register_blueprint(jogador)

db.create_all()