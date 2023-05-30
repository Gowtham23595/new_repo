from replit import clear
#HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

print("Welcome to Blind Auction")

g_bid_info_dict = []
g_winner = {}


def get_inputs():
    name = input("What is your name? ")
    bid_amount = int(input("What's you bid amount? $"))
    temp = {}
    temp["name"] = name
    temp["bid_amount"] = bid_amount
    g_bid_info_dict.append(temp)


def get_winner():
    max = 0
    name = ""
    for item in g_bid_info_dict:
        if max < int(item["bid_amount"]):
            max = item["bid_amount"]
            name = item["name"]

    print(f"The winner of the auction is {name} is ${max}")


def auction():
    get_inputs()
    flag = int(input("Are there any other bidders? 1 or 0"))
    while flag:
        clear()
        get_inputs()
        flag = int(input("Are there any other bidders? 1 or 0"))

    get_winner()


if __name__ == "__main__":
    auction()
