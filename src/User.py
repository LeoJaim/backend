from Container import Container

class User:
    def __init__(self, username, email, urlAvatar) -> None:
        self.username = username
        self.email = email
        self.urlAvatar = urlAvatar
        self.container = Container()
    
