from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import psycopg2

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

def get_db_connection():
    conn = psycopg2.connect(
        dbname="hotel_db", user="your_user", password="your_password", host="localhost"
    )
    return conn

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    # Проверка пользователя в базе данных
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Invalid credentials"}), 401

@app.route('/rooms', methods=['GET'])
@jwt_required()
def get_rooms():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM rooms')
    rooms = cursor.fetchall()
    conn.close()
    return jsonify(rooms), 200

if __name__ == '__main__':
    app.run(debug=True)

