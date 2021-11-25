class Admin:
    def __init__(self) -> None:
        self.list_users = []

    
    def observeUser(self, user):
        self.list_users.append(user)