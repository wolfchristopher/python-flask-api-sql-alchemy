from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
import os

user = os.getenv('DBUSER')
password = os.getenv('DBPASS')
host = os.getenv('DBHOST')
name =  os.getenv('DBNAME')
conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(user,password , host, name)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLAlCHEMY_DATABSE_URI'] = conn

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

def __init__(self, public_id, name, password,admin):
   self.public_id = public_id
   self.name = name
   self.password = password
   self.admin = admin

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