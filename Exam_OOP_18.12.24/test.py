def shop_report(self):
    unsold_plants = {}

    for plant in self.plants:
        if plant.name in unsold_plants:
            unsold_plants[plant.name] += 1
        else:
            unsold_plants[plant] = 1

    sorted_plants = sorted(unsold_plants.items(), key=lambda p: (-p[1]))
    sorted_clients = sorted(self.clients, key=lambda c: (-c.total_orders, c.phone_number))

    plants_result = []
    for name, count in sorted_plants:
        plants_result.append(f"{name}: {count}")

    clients_result = []
    for client in sorted_clients:
        clients_result.append(client.client_details())

    return (f"~Flower Shop Report~\n"
            f"Income: {self.income:.2f}\n"
            f"Count of orders: {sum(c.total_orders for c in self.clients)}\n"
            f"~~Unsold plants: {len(sorted_plants)}~~\n"
            f"{'\n'.join(plants_result)}\n"
            f"~~Clients number: {len(self.clients)}~~\n"
            f"{'\n'.join(clients_result)}")