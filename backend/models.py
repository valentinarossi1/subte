from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Panes(db.Model):
    __tablename__ = 'Panes'

    id_pan = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Integer, nullable=False)

    Pedido = db.relationship('Pedidos', backref='Panes')


class Bases(db.Model):
    __tablename__ = 'Bases'

    id_base = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Integer, nullable=False)

    Pedido = db.relationship('Pedidos', backref='Bases')


class Clientes(db.Model):
    __tablename__ = 'Clientes'

    id_cliente = db.Column(db.Integer, primary_key=True)
    nombre_apellido = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(255), nullable=False)
    mail = db.Column(db.String(255), nullable=False, unique=True)
    Pedido = db.relationship('Pedidos', backref='Clientes')


class Salsas(db.Model):
    __tablename__ = 'Salsas'

    id_salsa = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    Pedido = db.relationship('Pedidos', backref='Salsas')


class Adicionales(db.Model):
    __tablename__ = 'Adicionales'

    id_adicional = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    Pedido = db.relationship('Pedidos', backref='Adicionales')


class Pedidos(db.Model):
    __tablename__ = 'Pedidos'

    id_pedido = db.Column(db.Integer, primary_key=True)
    id_pan = db.Column(
        db.Integer, db.ForeignKey('Panes.id_pan'))
    id_base = db.Column(
        db.Integer, db.ForeignKey('Bases.id_base'))
    id_adicional = db.Column(
        db.Integer, db.ForeignKey('Adicionales.id_adicional'))
    id_salsa = db.Column(
        db.Integer, db.ForeignKey('Salsas.id_salsa'))
    mail = db.Column(
        db.String(255), db.ForeignKey('Clientes.mail'))

    pan = db.relationship('Panes', backref=db.backref('Pedidos', lazy=True))
