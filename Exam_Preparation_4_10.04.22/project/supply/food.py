from project.supply.supply import Supply


class Food(Supply):

    def __init__(self, name: str, energy: int = 25):
        Supply.__init__(self, name, energy)

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"