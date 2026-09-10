from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# User Model
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # This function MUST be inside the User class
    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }


# Create database tables
with app.app_context():
    db.create_all()


# Test route
@app.route('/test', methods=['GET'])
def test():
    return make_response(
        jsonify({'message': 'test route'}),
        200
    )


# Create a user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()

        new_user = User(
            username=data['username'],
            email=data['email']
        )

        db.session.add(new_user)
        db.session.commit()

        return make_response(
            jsonify({'message': 'user created'}),
            201
        )

    except Exception as e:
        db.session.rollback()
        return make_response(
        jsonify({'message': 'error creating user', 'error': str(e)}),
        500
    )


# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()

        return make_response(
            jsonify([user.json() for user in users]),
            200
        )

    except Exception as e:
        return make_response(
            jsonify({'message': 'error getting users', 'error': str(e)}),
            500
        )


# Get a user by ID
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    try:
        user = User.query.filter_by(id=id).first()

        if user:
            return make_response(
                jsonify({'user': user.json()}),
                200
            )

        return make_response(
            jsonify({'message': 'user not found'}),
            404
        )

    except Exception as e:
        return make_response(
            jsonify({'message': 'error getting user', 'error': str(e)}),
            500
        )


# Update a user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.filter_by(id=id).first()

        if user:
            data = request.get_json()

            user.username = data['username']
            user.email = data['email']

            db.session.commit()

            return make_response(
                jsonify({'message': 'user updated'}),
                200
            )

        return make_response(
            jsonify({'message': 'user not found'}),
            404
        )

    except Exception as e:
        db.session.rollback()
        return make_response(
        jsonify({'message': 'error updating user', 'error': str(e)}),
        500
    )


# Delete a user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()

        if user:
            db.session.delete(user)
            db.session.commit()

            return make_response(
                jsonify({'message': 'user deleted'}),
                200
            )

        return make_response(
            jsonify({'message': 'user not found'}),
            404
        )

    except Exception as e:
        db.session.rollback()
        return make_response(
        jsonify({'message': 'error deleting user', 'error': str(e)}),
        500
    )


# Run application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)