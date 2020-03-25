from myapp import db

class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    genero = db.Column(db.String(50))
    total_temporadas = db.Column(db.Integer)
    media_critica = db.Column(db.Float(asdecimal=True))
    ativa = db.Column(db.Boolean)

    def __init__(self, titulo, genero, total_temporadas, media_critica, ativa):
        self.titulo = titulo
        self.genero = genero
        self.total_temporadas = total_temporadas
        self.media_critica = media_critica
        self.ativa = ativa

    def __repr__(self):
        return 'Console {0}'.format(self.id)