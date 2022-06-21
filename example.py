#Step 1 
import random
from re import A
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
stage = []
for x in chosen_word:
    stage += "_"

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
while "_" in stage:
    guess = input("What letter? ").lower()


    for x in range(len(chosen_word)):
        letter = chosen_word[x]
        if letter == guess:
            stage[x] = guess
    print(stage,"\n")
print (f"You won! the word was {chosen_word}")