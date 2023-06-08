
class MenuItem:
    def __init__(self,name,cost,water,milk,coffee):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water":water,
            "milk":milk,
            "coffee":coffee
        }

class Menu:
    """Models of menu with Drinks"""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the items available in the menu"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self,drink_name):
        """Searches for the drink in the list"""
        for item in self.menu:
            if item.name == drink_name:
                return item
        print("Sorry that Item is not available")
        return 0