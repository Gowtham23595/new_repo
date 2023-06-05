import art
import random
import game_data
import os

print(art.logo)
def compare_followers(A,B):
    if A["follower_count"] > B["follower_count"]:
        return 1
    else:
        return 0


list_of_celeb = game_data.data

def app():
    lives = 1
    A = random.choice(list_of_celeb)
    print(f"Compare A : {A['name']} , a {A['description']} , from {A['country']}")
    print(art.vs)
    B = random.choice(list_of_celeb)
    while B == A:
        B = random.choice(list_of_celeb)
    print(f"Against B : {B['name']} , a {B['description']} , from {B['country']}")
    score = 0
    while lives != 0:
        user_input = input("Who has more followers? Type 'A' or 'B' : ")
        value = compare_followers(A,B)
        if value == 1:
            if user_input == 'A':
                A = B
                os.system('cls')
                score = score + 1
                print(f"Compare A : {A['name']} , a {A['description']} , from {A['country']}")
            else:
                lives = 0
                return score
        elif value == 0:
            if user_input == 'B':
                A = B
                os.system('cls')
                score = score + 1
                print(f"Compare A : {A['name']} , a {A['description']} , from {A['country']}")
            else:
                lives = 0
                return score
        print(art.vs)
        B = random.choice(list_of_celeb)
        while B == A:
            B = random.choice(list_of_celeb)
        print(f"Against B : {B['name']} , a {B['description']} , from {B['country']}")


if __name__ == "__main__":
    score = app()
    print(f"You have lost , Your final score {score}")