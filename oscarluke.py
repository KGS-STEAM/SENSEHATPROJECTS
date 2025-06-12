from sense_hat import SenseHat
from random import randint
from time import sleep
sense = SenseHat()
sense.show_message("welcome to maths warriors. In this game you will try to answer as many questions and minimising mistakes.", text_colour=[255, 0, 0],scroll_speed=0.05)
playerlives_1 = 3
playerlives_2 = 3 
num_correct = 0
num_correct_1 = 0
def easylevel():
  while playerlives_1 > 0:
    number = randint(1,100)
    number_1 = randint(1,100)
    message = (f"{number} + {number_1}")
    sense.show_message(message)
    answer = number + number_1
    guess = int(input())
    if guess == answer:
      num_correct = num_correct + 1
    if guess != answer:
      playerlives_1 = playerlives_1 - 1
def easy_level():
  while playerlives_2 > 0:
    number_2 = randint(1,100)
    number_3 = randint(1,100)
    message_1 = (f" {number_2} + {number_3}")
    sense.show_message(message_1)
    answer_1 = number_2 +number_3
    guess_1 = int(input())
    if guess_1 == answer_1:
      num_correct_1 = num_correct_1 + 1
    if guess_1 != answer_1:
      playerlives_2 = playerlives_2 - 1
def levelhard():
  while playerlives_1 > 0:
    number = randint(1,100)
    number_1 = randint(1,100)
    message = (f"{number} + {number_1}")
    sense.show_message(message)
    answer = number + number_1
    guess = int(input())
    if guess == answer:
      num_correct = num_correct + 1
    if guess != answer:
      playerlives_1 = playerlives_1 - 1
def level_hard():
  while playerlives_2 > 0:
    number_2 = randint(1,1000)
    number_3 = randint(1,1000)
    message_1 = (f" {number_2} + {number_3}")
    sense.show_message(message_1)
    answer_1 = number_2 +number_3
    guess_1 = int(input())
    if guess_1 == answer_1:
      num_correct_1 = num_correct_1 + 1
    if guess_1 != answer_1:
      playerlives_2 = playerlives_2 - 1
if num_correct > num_correct_1:
      sense.showm_message("player one has won")
if num_correct < num_correct_1:
      sense.show_message("player two has won.")
if num_correct == num_correct_1:
      sense.show_message("the game was a tie.")
sense.show_message("would you like to play easy or hard")
difficulty = input()
if input == "easy":
  leveleasy()
  level_easy()
if input == "hard":
    levelhard()
    level_hard()
