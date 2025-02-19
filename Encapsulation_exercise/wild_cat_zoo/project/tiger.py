from project.animal import Animal


class Tiger(Animal):

    def __init__(self, name: str, gender: str, age: int):
        Animal.__init__(self, name, gender, age, 45)