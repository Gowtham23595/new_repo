MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money_collected = []

def add_money(input):
    money_collected.append(input)

def report():
    print(f"Water  :{resources['water']}")
    print(f"Milk   :{resources['milk']}")
    print(f"coffee :{resources['coffee']}")
    print(f"Money   :$ {sum(money_collected)}")

def reduce_resources(water,milk,coffee):
    resources["water"] = resources["water"] - water
    resources["milk"] = resources["milk"] - milk
    resources["coffee"] = resources["coffee"] - coffee
    return
def check_resorces(water,milk,coffee):
    if water > resources['water']:
        print("Sorry there is not enough water")
        return 0
    elif milk > resources["milk"]:
        print("Sorry there is not enough milk")
        return 0
    elif coffee > resources["coffee"]:
        print("Sorry there is not enough coffee")
        return 0
    else:
        return 1

def get_coins():
    print("Please insert coins!")
    Quaters = int(input("How many quaters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return Quaters*0.25 + 0.1 * dimes + 0.05 * nickles + 0.01*pennies

def latte():
    water = MENU["latte"]["ingredients"]["water"]
    milk = MENU["latte"]["ingredients"]["milk"]
    coffee = MENU["latte"]["ingredients"]["coffee"]
    if check_resorces(water,milk,coffee) == 1:
        money_input = get_coins()
        if money_input > MENU["latte"]["cost"]:
            money_refund = money_input - MENU["latte"]["cost"]
            money_refund = '{:.2f}'.format(money_refund)
            print(f"Here is {money_refund} in change")
            print("Here is you latte enjoy")
            add_money(MENU["latte"]["cost"])
            reduce_resources(water,milk,coffee)
        else:
            print("Sorry that's not enough Money. Money Refunded")
    else:
        return

def espresso():
    water = MENU["espresso"]["ingredients"]["water"]
    milk = 0
    coffee = MENU["espresso"]["ingredients"]["coffee"]
    if check_resorces(water,milk,coffee) == 1:
        money_input = get_coins()
        if money_input > MENU["espresso"]["cost"]:
            money_refund = money_input - MENU["espresso"]["cost"]
            money_refund = '{:.2f}'.format(money_refund)
            print(f"Here is {money_refund} in change")
            print("Here is you espresso enjoy")
            add_money(MENU["espresso"]["cost"])
            reduce_resources(water,milk,coffee)
        else:
            print("Sorry that's not enough Money. Money Refunded")
    else:
        return

def cappuccino():
    water = MENU["cappuccino"]["ingredients"]["water"]
    milk = MENU["cappuccino"]["ingredients"]["milk"]
    coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    if check_resorces(water,milk,coffee) == 1:
        money_input = get_coins()
        if money_input > MENU["cappuccino"]["cost"]:
            reduce_resources(water,milk,coffee)
            money_refund = money_input - MENU["cappuccino"]["cost"]
            money_refund = '{:.2f}'.format(money_refund)
            print(f"Here is {money_refund} in change")
            print("Here is you cappuccino enjoy")
            add_money(MENU["cappuccino"]["cost"])
        else:
            print("Sorry that's not enough Money. Money Refunded")
    else:
        return


def app():
    user_input = True
    while user_input == True:
        user_input_coffee = input("What would you like?  (espresso/latte/cappuccino): ").lower()
        if user_input_coffee == "report":
            report()
        elif user_input_coffee == "off":
            user_input = False
        elif user_input_coffee == "espresso":
            espresso()
        elif user_input_coffee == "latte":
            latte()
        elif user_input_coffee == "cappuccino":
            cappuccino()
        else:
            print("Please enter a valid input")

if __name__ == "__main__":
    app()