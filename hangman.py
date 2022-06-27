#Step 1 
import random
from re import A
word_list = ["aardvark", "baboon", "camel"]
art = ['''
  +---+  
  |   |
  O   |
 /|\  |
 / \  |
      |
========
YOU LOSE
''']

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
stage = []
game = 1
lives = 3
for x in chosen_word:
    stage += "_"

while game:
    if "_" in stage:
        guess = input("What letter? ").lower()
        score = 0
        for x in range(len(chosen_word)):
            letter = chosen_word[x]
            if letter == guess:
                stage[x] = guess
                score += 1
        if score == 0:
            lives -= 1
            if lives == 0:
                print (art)
                print (f"The word was {chosen_word}")
                game = 0
            else:
                print (str(lives)+ " Lives Left")
        print(stage,"\n")
    else:
        print(f"You won! the word was {chosen_word}")
        game = 0
    