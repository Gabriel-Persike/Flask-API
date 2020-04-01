from myapp import db

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(100))
    Nickname = db.Column(db.String(100))
    Time = db.Column(db.String(100))
    Role = db.Column(db.String(100))
    Abates = db.Column(db.Integer)
    Assistencias = db.Column(db.Integer)
    Mortes = db.Column(db.Integer)
    Partidas = db.Column(db.Integer)
    Vitorias = db.Column(db.Integer)

    def __init__(self, Nome, Nickname, Time, Role, Abates, Assistencias, Mortes, Partidas, Vitorias):
        self.Nome = Nome
        self.Nickname = Nickname
        self.Time = Time
        self.Role = Role
        self.Abates = Abates
        self.Assistencias = Assistencias
        self.Mortes = Mortes
        self.Partidas = Partidas
        self.Vitorias = Vitorias

    def __repr__(self):
        return 'Jogador {0}'.format(self.id)

    def kdRatio(self):
        if self.Mortes>0:
            return (self.Abates + self.Assistencias)/self.Mortes
        else:
            return (self.Abates+ self.Assistencias)

    def WinRatio(self):
        if self.Partidas > 0:
            return (self.Vitorias/self.Partidas)*100
        else:
            return 0