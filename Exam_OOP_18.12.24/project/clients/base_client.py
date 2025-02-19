from abc import ABC, abstractmethod


class BaseClient(ABC):

    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number
        #THE DISCOUNT IS PERCENTAGE
        self.discount: float = 0.0
        self.total_orders: int = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Name must be at least two characters long!")
        
        self.__name = value
        
    @property
    def phone_number(self):
        return self.__phone_number

    #TODO CHECK THE ISDIGIT METHOD
    @phone_number.setter
    def phone_number(self, value):
        if not value.isdigit():
            raise ValueError("Phone number can contain only digits!")

        self.__phone_number = value

    @abstractmethod
    def update_discount(self):
        pass

    def update_total_orders(self):
        self.total_orders += 1

    #TODO MAYBE CHANGE INT ON DISCOUNT
    def client_details(self):
        return (f"Client: {self.name}, "
                f"Phone number: {self.phone_number}, "
                f"Orders count: {self.total_orders}, "
                f"Discount: {int(self.discount)}%")