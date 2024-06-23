from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Panes(db.Model):
    __tablename__ = 'Panes'

    id_pan = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Integer, nullable=False)


class Bases(db.Model):
    __tablename__ = 'Bases'

    id_base = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Integer, nullable=False)


class Clientes(db.Model):
    __tablename__ = 'Clientes'

    id_cliente = db.Column(db.Integer, primary_key=True)
    nombre_apellido = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)


class Salsas(db.Model):
    __tablename__ = 'Salsas'

    id_salsa = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Integer, nullable=False)


class Adicionales(db.Model):
    __tablename__ = 'Adicionales'

    id_adiccional = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Integer, nullable=False)


class Pedido(db.Model):
    __tablename__ = 'Pedido'

    id_pedido = db.Column(db.Integer, primary_key=True)
    id_pan = db.Column(
        db.Integer, db.ForeignKey('Panes.id_pan'), nullable=False)
    id_base = db.Column(
        db.Integer, db.ForeignKey('Bases.id_base'), nullable=False)
    id_cliente = db.Column(
        db.Integer, db.ForeignKey('Clientes.id_cliente'), nullable=False)
    id_adiccional = db.Column(
        db.Integer, db.ForeignKey('Adicionales.id_adiccional'), nullable=False)
    id_salsa = db.Column(
        db.Integer, db.ForeignKey('Salsas.id_salsa'), nullable=False)

    fecha = db.Column(db.Date, nullable=False)
    precio = db.Column(db.Integer, nullable=False)
