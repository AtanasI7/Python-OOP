from project.cat import Cat


class Tomcat(Cat):

    def __init__(self, name: str, age: int):
        Cat.__init__(self, name, age, "Male")

    @staticmethod
    def make_sound():
        return "Hiss"