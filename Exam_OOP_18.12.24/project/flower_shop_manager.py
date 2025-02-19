from typing import List
from project.clients.base_client import BaseClient
from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.base_plant import BasePlant
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant


class FlowerShopManager:
    VALID_PLANTS_TYPES = {
        "Flower": Flower,
        "LeafPlant": LeafPlant
    }
    VALID_CLIENTS_TYPES = {
        "RegularClient": RegularClient,
        "BusinessClient": BusinessClient
    }

    def __init__(self):
        self.income: float = 0.0
        self.plants: List[BasePlant] = []
        self.clients: List[BaseClient] = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        if plant_type not in self.VALID_PLANTS_TYPES:
            raise ValueError("Unknown plant type!")

        plant = self.VALID_PLANTS_TYPES[plant_type](plant_name, plant_price, plant_water_needed, plant_extra_data)
        self.plants.append(plant)

        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in self.VALID_CLIENTS_TYPES:
            raise ValueError("Unknown client type!")

        try:
            next(filter(lambda p: p.phone_number == client_phone_number, self.clients))
            raise ValueError("This phone number has been used!")

        except StopIteration:
            client = self.VALID_CLIENTS_TYPES[client_type](client_name, client_phone_number)
            self.clients.append(client)

            return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        try:
            client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients))
        except StopIteration:
            raise ValueError("Client not found!")

        #TODO MAYBE CHANGE THIS OR WHOLE METHOD
        plants = [p for p in self.plants if p.name == plant_name]
        if not plants:
            raise ValueError("Plants not found!")

        if len(plants) < plant_quantity:
            return f"Not enough plant quantity."

        #TODO MAYBE CHANGE
        for i in range(0, plant_quantity):
            self.plants.remove(plants[i])

        #TODO MAYBE NEED TO CHANGE THE DISCOUNT CALCULATION
        income_without_discount = plants[0].price * plant_quantity
        income = income_without_discount - (income_without_discount * client.discount / 100)
        self.income += income

        client.update_total_orders()
        client.update_discount()

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {income:.2f}"

    def remove_plant(self, plant_name: str):
        try:
            # plant = [p for p in self.plants if p.name == plant_name][0]
            plant = next(filter(lambda p: p.name == plant_name, self.plants))
        except StopIteration:
            return f"No such plant name."

        self.plants.remove(plant)
        return f"Removed {plant.plant_details()}"

    def remove_clients(self):
        clients_without_orders = [c for c in self.clients if c.total_orders == 0]

        #TODO MAYBE CHANGE CYCLE
        for i in range(0, len(clients_without_orders)):
            self.clients.remove(clients_without_orders[i])

        return f"{len(clients_without_orders)} client/s removed."

    def shop_report(self):
        income_report = f"Income: {self.income:.2f}"
        total_orders = sum(client.total_orders for client in self.clients)

        # Get the unsold plants and their count
        unsold_plants = {}
        for plant in self.plants:
            plant_name = plant.name
            if plant_name in unsold_plants:
                unsold_plants[plant_name] += 1
            else:
                unsold_plants[plant_name] = 1

        # Sort the unsold plants by count (descending) and by name (ascending)
        sorted_unsold_plants = sorted(unsold_plants.items(), key=lambda x: (-x[1], x[0]))

        # Prepare unsold plants section
        unsold_plants_report = "~~Unsold plants: {}~~".format(len(self.plants))
        unsold_plants_details = "\n".join([f"{name}: {count}" for name, count in sorted_unsold_plants])

        # Prepare client section, sorted by total orders (descending) and phone number (ascending)
        sorted_clients = sorted(self.clients, key=lambda c: (-c.total_orders, c.phone_number))
        clients_report = "~~Clients number: {}~~".format(len(self.clients))
        clients_details = "\n".join([client.client_details() for client in sorted_clients])

        # Combine everything into the full report
        report = f"~Flower Shop Report~\n{income_report}\nCount of orders: {total_orders}\n{unsold_plants_report}\n{unsold_plants_details}\n{clients_report}\n{clients_details}"

        return report
















