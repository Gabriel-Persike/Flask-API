import json
from flask import Blueprint, abort
from flask_restful import Resource, reqparse
from myapp.jogador.models import Jogador
from myapp import api, db

jogador = Blueprint('jogador', __name__)

parser = reqparse.RequestParser()
parser.add_argument('Nome', type=str)
parser.add_argument('Nickname', type=str)
parser.add_argument('Time', type=str)
parser.add_argument('Role', type=str)
parser.add_argument('Abates', type=int)
parser.add_argument('Assistencias', type=int)
parser.add_argument('Mortes', type=int)
parser.add_argument('Partidas', type=int)
parser.add_argument('Vitorias', type=int)


@jogador.route("/")
@jogador.route("/home")
def home():
    return "Jogadores de E-sports"

class JogadorAPI(Resource):
    def get(self, id=None, page=1):
        if not id:
            jogadores = Jogador.query.paginate(page,10).items
        else:
            jogadores = [Jogador.query.get(id)]
        if not jogadores :
            abort(404)
        res = {}
        for joga in jogadores:
            res[joga.id] = {
                "Nome": joga.Nome,
                "Nickname": joga.Nickname,
                "Time": joga.Time,
                "Role": joga.Role,
                "Abates": joga.Abates,
                "Assistencias": joga.Assistencias,
                "Mortes": joga.Mortes,
                "Partidas": joga.Partidas,
                "Vitorias": joga.Vitorias,
                "K+A/D": joga.kdRatio(),
                "Win Ratio": joga.WinRatio()
            }
        return json.dumps(res)

    def post(self):
        args = parser.parse_args()
        Nome = args['Nome']
        Nickname = args['Nickname']
        Time = args['Time']
        Role = args['Role']
        Abates = args['Abates']
        Assistencias = args['Assistencias']
        Mortes = args['Mortes']
        Partidas = args['Partidas']
        Vitorias = args['Vitorias']
    

        joga = Jogador(Nome, Nickname, Time, Role, Abates, Assistencias, Mortes, Partidas, Vitorias)
        db.session.add(joga)
        db.session.commit()
        res = {}
        res[joga.id] = {
            "Nome": joga.Nome,
            "Nickname": joga.Nickname,
            "Time": joga.Time,
            "Role": joga.Role,
            "Abates": joga.Abates,
            "Assistencias": joga.Assistencias,
            "Mortes": joga.Mortes,
            "Partidas": joga.Partidas,
            "Vitorias": joga.Vitorias
        }
        return json.dumps(res)

    def delete(self,id):
        joga = Jogador.query.get(id)
        db.session.delete(joga)
        db.session.commit()
        res = {"id": id}
        return json.dumps(res)

    def put(self, id):
        joga = Jogador.query.get(id)
        args = parser.parse_args()
        Nome = args['Nome']
        Nickname = args['Nickname']
        Time = args['Time']
        Role = args['Role']
        Abates = args['Abates']
        Assistencias = args['Assistencias']
        Mortes = args['Mortes']
        Partidas = args['Partidas']
        Vitorias = args['Vitorias']

        joga.Nome = Nome
        joga.Nickname = Nickname
        joga.Time = Time
        joga.Role = Role
        joga.Abates = Abates
        joga.Assistencias = Assistencias
        joga.Mortes = Mortes
        joga.Partidas = Partidas
        joga.Vitorias = Vitorias
    
        db.session.commit()
        res = {}
        res[joga.id] = {
            "Nome": joga.Nome,
            "Nickname": joga.Nickname,
            "Time": joga.Time,
            "Role": joga.Role,
            "Abates": joga.Abates,
            "Assistencias": joga.Assistencias,
            "Mortes": joga.Mortes,
            "Partidas": joga.Partidas,
            "Vitorias": joga.Vitorias
        }
        return json.dumps(res)

api.add_resource(
    JogadorAPI,
    '/api/jogador',
    '/api/jogador/<int:id>',
    '/api/jogador/<int:id>/<int:page>'
)