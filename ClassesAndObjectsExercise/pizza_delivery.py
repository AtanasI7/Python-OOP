class PizzaDelivery:

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False
        self.all_ingredients = []
        self.all_quantities = []

    def ordered(self):
        return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def add_extra(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return PizzaDelivery.ordered(self)

        # self.ingredients[ingredient] = self.ingredients.get(ingredient, 0) + quantity

        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
            self.price += price_per_quantity * quantity

        else:
            self.ingredients[ingredient] = quantity
            self.price += price_per_quantity * quantity

    def remove_ingredient(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return PizzaDelivery.ordered(self)

        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        if quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= quantity
        self.price -= price_per_quantity * quantity

    def make_order(self):
        self.ordered = True

        for i, q in self.ingredients.items():
            self.all_ingredients.append(i)
            self.all_quantities.append(q)

        return f"You've ordered pizza {self.name} prepared with {', '.join([f'{i}: {q}'for i, q in self.ingredients.items()])} and the price will be {self.price}lv."