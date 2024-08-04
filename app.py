from flask import Flask ,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (JWTManager,create_access_token,jwt_required,get_jwt_identity)
from passlib.hash import pbkdf2_sha256
import secrets

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = secrets.token_hex(32)
db = SQLAlchemy (app)
jwt = JWTManager(app)


#user model
class User(db.Model):
        id= db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        password = db.Column(db.String(200), nullable=False)

#Create the database

with app.app_context():
    db.create_all()

# User registration endpoint
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if User.query.filter_by(username = username).first():
        return jsonify({"msg": "Username already exists"}), 400
    hashed_password = pbkdf2_sha256.hash(password)
    new_user  = User(username = username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User registered successfully"}), 201

#user login endpoint
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json() 
    username = data.get("username")
    password = data.get("password")
    user = User.query.filter_by(username=username).first()
    if not user or not pbkdf2_sha256.verify(password, user.password): 
        return jsonify({"msg": "Invalid username or password"}), 401
    access_token = create_access_token(identity=username) 
    return jsonify(access_token=access_token), 200

#Protected endpoint
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == "__main__":
    app.run(debug=True)

