from flask import Blueprint, request, jsonify
from app import db
from app.models import User

# blueprint
main = Blueprint('main', __name__)

# стартовая страница
@main.route('/', methods=['GET'])
def index():
    return "welcome to the book club backend"

# страница с регистрацией/логином
@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"error": "Invalid input"}), 400

    # проверка уже существующего пользователя
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already registered"}), 400

    # Create a new user
    user = User(email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201
