
class User:
    def __init__(self, id, username, date, password_hash):
        self.id = id
        self.username = username
        self.date = date
        self.password_hash = password_hash
        self.post_number = 0
        self.comment_number = 0
