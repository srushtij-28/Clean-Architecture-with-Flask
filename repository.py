from models import db, User

class UserRepository:

    def create(self, name):

        user = User(name=name)

        db.session.add(user)
        db.session.commit()

        return user

    def get_all(self):

        return User.query.all()
