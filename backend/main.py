from flask import Flask, request, jsonify
from models import db, Usuarios, Panes, Pedido


app = Flask(__name__)
port = 5000

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def hello_world():
    return "hello world"


@app.route("/data/<section>")
def data(section):
    return section


if __name__ == '__main__':
    print('Starting server...')
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', debug=True, port=port)
    print('Started...')
