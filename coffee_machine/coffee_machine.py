class CoffeeMaker:

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints all the reports that are present"""
        print(f"Water  :{self.resources['water']}ml")
        print(f"Milk   :{self.resources['milk']}ml")
        print(f"coffee :{self.resources['coffee']}g")

    def is_resource_sufficient(self,drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
