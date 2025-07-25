from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sura(db.Model):
    num_sura = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)

class Ayat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sura = db.Column(db.Integer, db.ForeignKey('sura.num_sura'), nullable=False)
    num_aya = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
