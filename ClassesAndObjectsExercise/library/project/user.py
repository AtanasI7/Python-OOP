class User:

    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def info(self):
        return ', '.join(sorted(self.books)) or "[]"

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.info()}"


user = User(123123, 'IVAN')
