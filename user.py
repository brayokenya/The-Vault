# Create account class
class User:
    """
    class that creates instances of a user
    """
    users = []

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def save_user(self):
        """
        This method saves user objects to the users list
        """
        User.users.append(self)

    def login(self):
        """
        This method checks if a user object exists in the users list
        """
        if User in User.users:
            print(User)
            return User
