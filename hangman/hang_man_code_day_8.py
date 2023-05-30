#Step 2

import random
import hanng_man_words as hm
import hang_man_art as hm_art

word_list = hm.word_list
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

Number_of_lives = len(hm_art.stages)
Number_of_correct_instances = word_length

while Number_of_lives != 0:
    guess = input("Guess a letter: ").lower()
    flag = 0
    if Number_of_correct_instances != 0:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess and display[position] != letter:
                display[position] = letter
                Number_of_correct_instances -= 1
                flag = 1
    if Number_of_lives > 0 and Number_of_correct_instances == 0:
        print("User Guessed the correct word")
        print(display)
        break
    if flag == 0:
        Number_of_lives -= 1
        print("you guessed the wrong word")
        print(f"Number of lives remaining {Number_of_lives}")
        print(hm_art.stages[Number_of_lives])
    if (Number_of_lives == 0):
        print("You failed to guess")
        break

    print(display)

print(display)
