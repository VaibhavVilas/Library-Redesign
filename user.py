from models import User
from storage import Storage

# template of UserManager to manage users


class UserManager:

    # defining attributes for users.json file where users will be stored
    def __init__(self, file_path='users.json'):
        self.file_path = file_path
        self.users = self.load_users()

    # method to load/read users from users.json
    def load_users(self):
        users_data = Storage.load_data(self.file_path)
        return [User(**user) for user in users_data]

    # method to save users in users.json
    def save_users(self):
        users_data = [user.__dict__ for user in self.users]
        Storage.save_data(self.file_path, users_data)

    # method to check whether a user is present or not.
    def is_user_present(self, user_id):
        # since user_id is unique for every user we base our check on that
        return any(user.user_id == user_id for user in self.users)

    # method to add a user
    def add_user(self, name, user_id):

        # check if the given user already exists
        if self.is_user_present(user_id):
            print('\nUser already exists in the library!')
            return

        # appending the given user and saving it in users.json
        user = User(name, user_id)
        self.users.append(user)
        self.save_users()
        print('\nUser Added')
