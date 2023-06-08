from coffee_machine import CoffeeMaker
from money_machine import MoneyMachine
from menu import MenuItem,Menu


def app():
    user_flag = True
    menu = Menu()
    cm = CoffeeMaker()
    mm = MoneyMachine()
    while user_flag == True:
        user_input = input(f"What would you like?  {menu.get_items()}: ").lower()
        if user_input == "report":
            cm.report()
        elif user_input == "off":
            user_flag = False
        else:
            drink =  menu.find_drink(user_input)
            if drink != 0:
                if cm.is_resource_sufficient(drink):
                    if mm.make_payment(drink.cost):
                        cm.make_coffee(drink)






if __name__ == "__main__":
    app()