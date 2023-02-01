from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS, cross_origin

api = Blueprint('api', __name__)
CORS(api)

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = jsonify(message="Simple server is running")
    response_body.headers.add("Access-Control-Allow-Origin", "*")
    return response_body, 200

@api.route("/signup", methods=["POST"])
@cross_origin()
def signup():
    if request.method == 'POST':
        email = request.json.get('email', None)
        username = request.json.get('username', None)
        password = request.json.get('password', None)

        if not email:
            return 'Email is required', 401
        if not username:
            return 'Username is required', 401
        if not password:
            return 'Password is required', 401
        
        email_query = User.query.filter_by(email=email).first()
        if email_query:
            return 'This email already exists' , 402
        user = User()
        user.email = email
        user.username = username
        user.password = password
        user.is_active = True
        print(user)
        db.session.add(user)
        db.session.commit()

        response = {
            'msg': 'User added successfully',
            'email': email,
            'username': username
        }
        return jsonify(response), 200

