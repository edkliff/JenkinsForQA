from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    is_blocked = db.Column(db.Integer)
    permissions = db.Column(db.Integer)

    def set_passwd(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Servers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(64), index=True, unique=True)
    branch = db.Column(db.String(64))

    def get_server(self, address, branch):
        self.address = address
        self.branch = branch


@login.user_loader
def get_user(user_id):
    return Users.query.get(int(user_id))