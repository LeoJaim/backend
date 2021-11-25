from Admin import Admin
from Reporter import Reporter
from User import User

class System():

    def __init__(self) -> None:
        self.admin = Admin()
        self.reporter = Reporter()
        self.users = [User(), User(), User()]

    def newUser(self, user: User) -> None:
        self.users.append(user)
        self.admin.observeUser(user)