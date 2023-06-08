class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.money_collected = 0
        self.profit = 0

    def report(self):
        """Print the current profit"""
        print(f"Money : {self.CURRENCY}{self.profit}")

    def process_coins(self):
        "Returns the total calculated coins"
        for coin in self.COIN_VALUES:
            self.money_collected += int(input(f"How many {coin}? ")) * self.COIN_VALUES[coin]
        return self.money_collected

    def make_payment(self,cost):
        self.process_coins()
        if self.money_collected >= cost :
            change = round(self.money_collected - cost, 2)
            print(f"Here is the change {self.CURRENCY}{change}")
            self.profit +=cost
            self.money_collected = 0
            return 1
        else:
            print("Sorry that's not enough Money. Money Refunded")
            return 0
