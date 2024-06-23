from flask_cors import CORS
from flask import Flask, jsonify, request
from models import db, Clientes, Panes


app = Flask(__name__)
CORS(app)

port = 5000

base_datos = 'postgresql+psycopg2://postgres:postgres@localhost:5432/subte'
app.config['SQLALCHEMY_DATABASE_URI'] = base_datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def hello_world():
    return jsonify({'message': 'hola mundo'})


@app.route("/panes", methods=['GET'])
def Listar_panes():

    try:

        panes = Panes.query.all()
        panes_datos = []

        for pan in panes:
            dato_pan = {
                'id_pan': pan.id_pan,
                'nombre': pan.nombre,
                'precio': pan.precio
            }
            panes_datos.append(dato_pan)

        return jsonify(panes_datos)

    except Exception as e:

        return jsonify(f"Error {e}"), 404


@app.route("/clientes", methods=['GET'])
def Listar_clientes():

    try:

        clientes = Clientes.query.all()
        clientes_datos = []

        for cliente in clientes:
            dato_cliente = {
                'id': cliente.id_cliente,
                'nombre': cliente.nombre_apellido,
                'direccion': cliente.direccion
            }
            clientes_datos.append(dato_cliente)

        return jsonify(clientes_datos)

    except Exception as e:

        return jsonify(f"Error {e}"), 404


@app.route("/clientes/<id_cliente>", methods=['GET'])
def data_cliente(id_cliente):

    cliente = Clientes.query.get(id_cliente)
    try:

        cliente_datos = {
            'id': cliente.id_cliente,
            'nombre': cliente.nombre_apellido,
            'direccion': cliente.direccion
        }

        return cliente_datos

    except Exception as e:

        return jsonify(f"Error {e}:  {id_cliente}"), 404


@app.route("/clientes", methods=["POST"])
def nuevo_usuario():

    data = request.json
    try:
        nuevo_nombre = data.get('nombre_apellido')
        nueva_direccion = data.get('direccion')
        nuevo_telefono = data.get('telefono')

        nuevo_cliente = Clientes(nombre_apellido=nuevo_nombre,
                                 direccion=nueva_direccion,
                                 telefono=nuevo_telefono)

        db.session.add(nuevo_cliente)
        db.session.commit()

        return jsonify(
            {'cliente':
                {'id_cliente': nuevo_cliente.id_cliente,
                 'name': nuevo_cliente.nombre_apellido,
                 'precio': nuevo_cliente.telefono}}
        ), 201

    except Exception as e:
        return jsonify(f"no se  pudo :{e})"), 400


if __name__ == '__main__':
    print('Starting server...')
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', debug=True, port=port)
    print('Started...')
