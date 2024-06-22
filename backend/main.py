from flask_cors import CORS
from flask import Flask, request, jsonify
from models import db, Clientes


app = Flask(__name__)
CORS(app)

port = 5000

base_datos = 'postgresql+psycopg2://postgres:postgres@localhost:5432/subte'
app.config['SQLALCHEMY_DATABASE_URI'] = base_datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def hello_world():
    return jsonify({'message': 'hola mundo'})


@app.route("/cliente/<id_cliente>")
def data_cliente(id_cliente):
    cliente = Clientes.query.where(Clientes.id_cliente == id_cliente).first()

    cliente_datos = {
        'id': cliente.id_cliente,
        'nombre': cliente.nombre_apellido,
        'direccion': cliente.direccion
    }

    return cliente_datos


if __name__ == '__main__':
    print('Starting server...')
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', debug=True, port=port)
    print('Started...')
