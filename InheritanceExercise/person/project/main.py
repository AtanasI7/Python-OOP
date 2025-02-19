from project.child import Child
from project.person import Person

person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__)

# __class__ връща класа като обект
# __bases__ връща класовете които наследяваме, [0] - първия наследен клас; [1] - втори наследен клас и т.н.
# __name__ връща името на класа