from project.animal import Animal


class Cheetah(Animal):

    def __init__(self, name: str, gender: str, age: int):
        Animal.__init__(self, name, gender, age, 60)