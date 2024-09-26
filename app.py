from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mibasededatos.db'
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Hello, World!"})

@app.route('/createUser', methods=['POST'])
def create():
    data = request.json
    usuario = User()

    usuario.nombre = data['nombre']
    usuario.apellido = data['apellido']
    usuario.email = data['email']
    usuario.password = data['password']

    db.session.add(usuario)
    db.session.commit()

    return{
        "message": "User created successfully",
        "data": usuario.serialize()
    }, 201

if __name__== "__main__":
    app.run(host='localhost', port=5002, debug=True)