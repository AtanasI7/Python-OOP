from typing import List
from project.animal import Animal
from project.worker import Worker

class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return 'Not enough budget'

        return 'Not enough space for animal'

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return 'Not enough space for worker'

    def fire_worker(self, worker_name: str):
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            # worker = next(filter(lambda w: w.name == worker_name, self.workers))       И двата начина работят!!!!!!!!!!!

            self.workers.remove(worker)
            return f"{worker_name} fired successfully"

        except IndexError:
        # except StopIteration:
            return f"There is no {worker_name} in the zoo"


    def pay_workers(self):
        money_to_pay = sum([w.salary for w in self.workers])

        if money_to_pay <= self.__budget:
            self.__budget -= money_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_to_feed_animals = sum([a.money_for_care for a in self.animals])

        if self.__budget >= money_to_feed_animals:
            self.__budget -= money_to_feed_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"

        lions = [a for a in self.animals if a.__class__.__name__ == 'Lion']
        result += f"----- {len(lions)} Lions:\n"
        for l in lions:
            result += f"{l}\n"

        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        result += f"----- {len(tigers)} Tigers:\n"
        for t in tigers:
            result += f"{t}\n"

        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for c in cheetahs:
            result += f"{c}\n"

        return result[:-1]

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = [w for w in self.workers if w.__class__.__name__ == 'Keeper']
        result += f"----- {len(keepers)} Keepers:\n"
        for k in keepers:
            result += f"{k}\n"

        caretakers = [w for w in self.workers if w.__class__.__name__ == 'Caretaker']
        result += f"----- {len(caretakers)} Caretakers:\n"
        for c in caretakers:
            result += f"{c}\n"

        vets = [w for w in self.workers if w.__class__.__name__ == 'Vet']
        result += f"----- {len(vets)} Vets:\n"
        for v in vets:
            result += f"{v}\n"

        return result[:-1]

# w = Worker('Ivan', 12, 15)
# pederas = Worker('Pederas', 13, 20)
# z = Zoo('dateeba', 1100101011, 10, 10)
# print(z.hire_worker(w))
# print(z.hire_worker(pederas))
# print(z.fire_worker('Ivan'))