import art
import random

print(art.logo)

def guess_the_number(guess_number,number):
    if guess_number > number:
        print("Too HIGH\nGuess Again")
        return -1
    elif guess_number < number:
        print("Too LOW\nGuess Again")
        return -1
    else:
        return 1

guessed_number = []

def app():
    print("Welcome to the number Guessing game")
    print("I am thinking of a number between 1 to 100")
    number = random.randint(1,100)
    difficulty_setting = input("Choose a difficulty setting! Type 'easy' or 'hard' : ").lower()
    if difficulty_setting == "easy":
        number_of_lives = 10
    else:
        number_of_lives = 5

    while number_of_lives != 0:
        print(f"The numbers that you have tried {guessed_number} ")
        guess = int(input("Make a Guess: "))
        guessed_number.append(guess)
        flag = guess_the_number(guess,number)
        if flag == 1:
            print(f"You got it , The answer was {number}")
            return
        else:
            number_of_lives = number_of_lives - 1
            print(f"You have {number_of_lives} attempts to guess the number")
    if number_of_lives == 0:
        print(f"The correct number is {number}. Better luck next time !!!")

if __name__ == "__main__":
    app()