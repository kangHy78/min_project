from werkzeug.security import check_password_hash
from flask_login import UserMixin

from apps.app import db, login_manager


class Cafe(db.Model):
    __tablename__ = "cafes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    text = db.Column(db.String)



class Admin(UserMixin, db.Model):
    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    @property
    def password(self):
        return self.password_hash

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    


@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(user_id)