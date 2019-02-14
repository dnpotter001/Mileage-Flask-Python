from mileage import bcrypt
from flask_login import UserMixin

class User():

    def __init__(self, user_id, displayName):
        self._id  = user_id
        self.displayName = displayName

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self._id
        
    @staticmethod
    def validate_login(password_hash, password):
        return bcrypt.check_password_hash(password_hash, password)