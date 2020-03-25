import json
from flask import Blueprint, abort
from flask_restful import Resource, reqparse
from myapp.console.models import Console
from myapp import api, db

console = Blueprint('console', __name__)

parser = reqparse.RequestParser()
parser.add_argument('titulo', type=str)
parser.add_argument('genero', type=str)
parser.add_argument('total_temporadas', type=int)
parser.add_argument('media_critica', type=float)
parser.add_argument('ativa', type=bool)

@console.route("/")
@console.route("/home")
def home():
    return "Catálogo de Séries"

class ConsoleAPI(Resource):
    def get(self, id=None, page=1):
        if not id:
            consoles = Console.query.paginate(page,10).items
        else:
            consoles = [Console.query.get(id)]
        if not consoles :
            abort(404)
        res = {}
        for con in consoles:
            res[con.id] = {
                'titulo': con.titulo,
                'genero': con.genero,
                'total_temporadas': con.total_temporadas,
                'media_critica': str(con.media_critica),
                'ativa': con.ativa
            }
        return json.dumps(res)

    def post(self):
        args = parser.parse_args()
        titulo = args['titulo']
        genero = args['genero']
        total_temporadas = args['total_temporadas']
        media_critica = args['media_critica']
        ativa = args['ativa']

        con = Console(titulo, genero, total_temporadas, media_critica, ativa)
        db.session.add(con)
        db.session.commit()
        res = {}
        res[con.id] = {
            'titulo': con.titulo,
            'genero': con.genero,
            'total_temporadas': con.total_temporadas,
            'media_critica': str(con.media_critica),
            'ativa': con.ativa
        }
        return json.dumps(res)

api.add_resource(
    ConsoleAPI,
    '/api/console',
    '/api/console/<int:id>',
    '/api/console/<int:id>/<int:page>'
)