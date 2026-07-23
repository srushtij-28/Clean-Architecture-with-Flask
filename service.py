from repository import UserRepository

class UserService:

    def __init__(self):

        self.repository = UserRepository()

    def create_user(self, name):

        return self.repository.create(name)

    def list_users(self):

        return self.repository.get_all()
