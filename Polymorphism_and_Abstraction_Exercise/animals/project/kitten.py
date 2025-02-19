from project.cat import Cat


class Kitten(Cat):

    def __init__(self, name: str, age: int):
        Cat.__init__(self, name, age, "Female")

    @staticmethod
    def make_sound():
        return "Meow"