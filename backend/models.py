import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Usuarios(db.Model):
    __tablename__ = 'Usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    # algun otro atributo


class Panes(db.Model):
    __tablename__ = 'Panes'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    # algun otro atributo


class rellenos(db.Model):
    __tablename__ = 'Rellenos'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    # algun otro atributo


class Pedido(db.Model):
    __tablename__ = 'Pedido'
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(
        db.Integer, db.ForeignKey('Usuarios.id'), nullable=False)
    tipo_pan = db.Column(db.Integer, db.ForeignKey('Panes.id'), nullable=False)
    tipo_relleno = db.Column(db.Integer, db.ForeignKey(
        'Rellenos.id'), nullable=False)
    precio = db.Column(db.Integer, nullable=False)

    # relacion entre tablas
    pan = db.relationship("Panes", foreign_keys=[tipo_pan])
    relleno = db.relationship("Rellenos", foreign_keys=[tipo_relleno])
    usuario = db.relationship("Usuarios", foreign_keys=[id_usuario])
