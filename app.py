from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
import secrets

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLAlCHEMY_DATABSE_URI'] = conn

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary=True)
    public_id = db.Colomn(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

@app.route('/user', methods=['GET'])
def get_all_users():
    return ''

@app.route('/user/<user_id>', methods=['GET'])
def get_user():
    return ''

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = Users(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_password, admin=False)
    db.session.ass(new_user)
    db.session.commit()
    return jsonify({'message' : 'New User created!'})

@app.route('/user/<user_id>', methods=['PUT'])
def update_user():
    return ''

@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user():
    return ''

if __name__ == '__name__':
    db.create_all()
    app.run(debug=True)