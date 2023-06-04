############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import art

print(art.logo)


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    card = random.choice(cards)
    return card

def calculate_score(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
        if sum > 21 and (i != len(list) - 1):
            if 11 in list:
                sum = sum - 10
    return sum


class check_black_jack():

    def __init__(self):
        self.user_score, self.computer_score = 0, 0
        self.user_cards = []
        self.computer_cards = []
        for i in range(2):
            self.user_cards.append(deal_card())
            self.computer_cards.append(deal_card())
            self.user_score = calculate_score(self.user_cards)
            self.computer_score = calculate_score(self.computer_cards)

    def _main(self):
        print(f"User cards {self.user_cards}")
        print(f"Computer cards {self.computer_cards[0]}")
        if self.user_score < 21:
            user_input = input("Do you want to deal another card? yes or no ")
            while user_input == "yes":
                card = int(deal_card())
                self.user_cards.append(card)
                self.user_score = calculate_score(self.user_cards)
                if self.user_score < 21:
                    print(f"User cards {self.user_cards}")
                    print(f"Computer cards {self.computer_cards[0]}")
                    user_input = input(
                        "Do you want to deal another card? yes or no ")
                else:
                    user_input = "no"
        if (self.user_score == 21 or self.user_score > 21):
            self.compare_cards(self.user_score, self.computer_score)
            return
        while calculate_score(self.computer_cards) < 17:
            card = int(deal_card())
            self.computer_cards.append(card)
            self.computer_score = calculate_score(self.computer_cards)
        self.compare_cards(self.user_score, self.computer_score)
        return

    def clear(self):
        self.user_score = 0
        self.user_cards = []
        self.computer_cards = []

    def compare_cards(self, user_score, computer_score):
        if computer_score == 0 or user_score == 0:
            if computer_score == 0:
                print(f"Computer Wins{self.computer_cards}")
                print(f"User loses{self.user_cards}")
            else:
                print(f"User wins{self.user_cards}")
                print(f"Computer loses{self.computer_cards}")
        elif (computer_score > 21) or (user_score > 21):
            if computer_score > 21:
                print(f"User wins{self.user_cards}")
                print(f"Computer loses{self.computer_cards}")
            else:
                print(f"Computer Wins{self.computer_cards}")
                print(f"User loses{self.user_cards}")
        else:
            if (user_score > computer_score):
                print(f"User wins{self.user_cards}")
                print(f"Computer loses{self.computer_cards}")
            else:
                print(f"Computer Wins{self.computer_cards}")
                print(f"User loses{self.user_cards}")


if __name__ == "__main__":
    user_input = input(
        "Do you want to play black_jack? yes or no ").lower().strip()
    obj1 = check_black_jack()
    while user_input == "yes":
        obj1._main()
        user_input = input(
            "Do you want to continue play black_jack? yes or no ").lower(
            ).strip()
        obj1.clear()
        obj1.__init__()
    if user_input != "yes":
        print("Thanks for playing black jack see you soon\n")

