from flask_cors import CORS
from flask import Flask, jsonify, request, render_template
from models import db, Clientes, Panes, Pedidos, Bases, Salsas, Adicionales


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
                'direccion': cliente.direccion,
                'telefono': cliente.telefono,
                'mail': cliente.mail
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


@app.route("/pedidos", methods=['GET'])
def Listar_pedidos():

    try:
        pedidos_con_nombres = Pedidos.query.join(
            Panes, Panes.id_pan == Pedidos.id_pan
        ).join(
            Bases, Bases.id_base == Pedidos.id_base
        ).join(
            Adicionales, Adicionales.id_adicional == Pedidos.id_adicional
        ).join(
            Salsas, Salsas.id_salsa == Pedidos.id_salsa
        ).join(
            Clientes, Clientes.mail == Pedidos.mail
        )

        pedidos_datos = []
        for pedido in pedidos_con_nombres:
            dato_pedido = {
                'id_pedido': pedido.id_pedido,
                'pan': pedido.Panes.nombre,
                'base': pedido.Bases.nombre,
                'adicional':
                pedido.Adicionales.nombre if pedido.Adicionales else None,
                'salsa': pedido.Salsas.nombre,
                'mail': pedido.Clientes.mail,
            }
            pedidos_datos.append(dato_pedido)

        return jsonify(pedidos_datos)

    except Exception as e:
        return jsonify(f"Error {e}"), 404


@app.route("/pedidos/<id>", methods=['GET'])
def Listar_pedidos_id(id):

    pedido = Pedidos.query.get(id)
    try:

        pedido_dato = {
            'pan': pedido.id_pan,
            'base': pedido.id_base,
            'adicional': pedido.id_adicional,
            'salsa': pedido.id_salsa,
            'mail': pedido.mail
        }

        return jsonify(pedido_dato)

    except Exception as e:
        return jsonify(f"Error {e}"), 404


@ app.route("/pedidos", methods=["POST"])
def nuevo_pedido():

    data = request.json
    if data is None:
        return jsonify({'error': 'No se recibieron datos'}), 400
    try:
        nuevo_pan = data.get('id_pan')
        nueva_base = data.get('id_base')
        nuevo_adicional = data.get('id_adicional')
        nuevo_salsa = data.get('id_salsa')
        nuevo_cliente = data.get('mail')

        nuevo_pedido = Pedidos(id_pan=nuevo_pan,
                               id_base=nueva_base,
                               id_adicional=nuevo_adicional,
                               id_salsa=nuevo_salsa,
                               mail=nuevo_cliente)
        db.session.add(nuevo_pedido)
        db.session.commit()

        return jsonify(
            {'pedido':
                {'pan': nuevo_pedido.id_pan,
                 'base': nuevo_pedido.id_base,
                 'adicional': nuevo_pedido.id_adicional,
                 'salsa': nuevo_pedido.id_salsa,
                 'mail': nuevo_pedido.mail}}

        ), 201

    except Exception as e:
        return jsonify(f"no seaaaaaaaaaaaaaa  pudo :{e})"), 400


@app.route("/mail/<mail_url>", methods=['GET'])
def pedidos_mail(mail_url):

    try:
        cliente = Clientes.query.filter_by(mail=mail_url).first()

        if not cliente:
            return jsonify({'error': 'Cliente no encontrado'}), 404

        pedidos_con_nombres = Pedidos.query.join(
            Panes, Panes.id_pan == Pedidos.id_pan
        ).join(
            Bases, Bases.id_base == Pedidos.id_base
        ).join(
            Adicionales, Adicionales.id_adicional == Pedidos.id_adicional
        ).join(
            Salsas, Salsas.id_salsa == Pedidos.id_salsa
        ).filter(Pedidos.mail == mail_url).all()

        pedidos_datos = []
        for pedido in pedidos_con_nombres:
            dato_pedido = {
                'pan': pedido.Panes.nombre,
                'base': pedido.Bases.nombre,
                'adicional':
                pedido.Adicionales.nombre if pedido.Adicionales else None,
                'salsa': pedido.Salsas.nombre,
                'mail': pedido.Clientes.mail,
            }
            pedidos_datos.append(dato_pedido)

        return jsonify(pedidos_datos)

    except Exception as e:
        return jsonify(f"Error {e}"), 404


@ app.route("/clientes", methods=["POST"])
def nuevo_cliente():

    data = request.json

    if data is None:
        return jsonify({'error': 'No se recibieron datos'}), 400

    try:
        nuevo_nombre = data.get('nombre_apellido')
        nueva_direccion = data.get('direccion')
        nuevo_telefono = data.get('telefono')
        nuevo_mail = data.get('mail')

        nuevo_cliente = Clientes(nombre_apellido=nuevo_nombre,
                                 direccion=nueva_direccion,
                                 telefono=nuevo_telefono, mail=nuevo_mail)
        db.session.add(nuevo_cliente)
        db.session.commit()

        return jsonify(
            {'cliente':
                {'nombre_apellido': nuevo_cliente.nombre_apellido,
                 'direccion': nuevo_cliente.direccion,
                 'telefono': nuevo_cliente.telefono,
                 'mail': nuevo_cliente.mail}}

        ), 201

    except Exception as e:
        return jsonify(f"no se  pudo :{e})"), 400


@app.route("/mostrar_datos/<mail>/<pan>/<base>/<adicional>/<salsa>",
           methods=['GET'])
def datos(mail, pan, base, adicional, salsa):

    try:
        nombre_cliente = Clientes.query.filter_by(mail=mail).first()
        nombre_pan = Panes.query.get(pan)
        nombre_base = Bases.query.get(base)
        nombre_adicional = Adicionales.query.get(adicional)
        nombre_salsa = Salsas.query.get(salsa)
        precio = nombre_pan.precio+nombre_pan.precio + \
            nombre_adicional.precio+nombre_salsa.precio

        cliente_datos = {
            'nombre': nombre_cliente.nombre_apellido,
            'mail': mail,
            'pan': nombre_pan.nombre,
            'base': nombre_base.nombre,
            'adicional': nombre_adicional.nombre,
            'salsa': nombre_salsa.nombre,
            'precio': precio
        }
        return jsonify(cliente_datos), 200

    except Exception as e:

        return jsonify(f"Error {e}:  {mail}"), 404


@ app.errorhandler(404)
def pagina_no_encontrada(error):

    return render_template('./404.html'), 404


def init_db():
    if not Panes.query.first():
        panes = [
            Panes(nombre='Pan INTENTO', precio=5),
            Panes(nombre='Pan de', precio=6),
            Panes(nombre='Pan INITIAZIACION', precio=7),
            Panes(nombre='Pan INITIAZIACION', precio=7)
        ]
        db.session.bulk_save_objects(panes)

    if not Bases.query.first():
        bases = [
            Bases(nombre='Pan INTENTO', precio=5),
            Bases(nombre='Pan INTENTO', precio=5),
            Bases(nombre='Pan INTENTO', precio=5),
            Bases(nombre='Pan INTENTO', precio=5)
        ]
        db.session.bulk_save_objects(bases)

    if not Salsas.query.first():
        salsas = [
            Salsas(nombre='Pan INTENTO', precio=5),
            Salsas(nombre='Pan INTENTO', precio=5),
            Salsas(nombre='Pan INTENTO', precio=5),
            Salsas(nombre='Pan INTENTO', precio=5),
        ]
        db.session.bulk_save_objects(salsas)

    if not Adicionales.query.first():
        adicionales = [
            Adicionales(nombre='Pan INTENTO', precio=5),
            Adicionales(nombre='Pan INTENTO', precio=5),
            Adicionales(nombre='Pan INTENTO', precio=5),
            Adicionales(nombre='Pan INTENTO', precio=5),
        ]
        db.session.bulk_save_objects(adicionales)
    db.session.commit()


if __name__ == '__main__':
    print('Starting server...')
    db.init_app(app)
    with app.app_context():
        db.create_all()
        init_db()

    app.run(host='0.0.0.0', debug=True, port=port)
    print('Started...')
