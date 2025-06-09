from sense_hat import SenseHat
from random import randint
import random
from time import sleep
sense = SenseHat()
player = 1
dice_number = ["one", "two", "three", "four", "five", "six"]
b = (135, 38, 81)
c = (255, 255, 255)
one = [
  c, c, c, c, c, c, c, c,
  c, c, c, c, c, c, c, c,
  c, c, c, c, c, c, c, c,
  c, c, c, b, b, c, c, c,
  c, c, c, b, b, c, c, c,
  c, c, c, c, c, c, c, c,
  c, c, c, c, c, c, c, c,
  c, c, c, c, c, c, c, c
]
two = [
  c, c, c, c, c, c, c, c,
  c, c, c, c, c, b, b, c,
  c, c, c, c, c, b, b, c,
  c, c, c, c, c, c, c, c,
  c, c, c, c, c, c, c, c,
  c, b, b, c, c, c, c, c,
  c, b, b, c, c, c, c, c,
  c, c, c, c, c, c, c, c
]
three = [
  c, c, c, c, c, c, b, b,
  c, c, c, c, c, c, b, b,
  c, c, c, c, c, c, c, c,
  c, c, c, b, b, c, c, c,
  c, c, c, b, b, c, c, c,
  c, c, c, c, c, c, c, c,
  b, b, c, c, c, c, c, c,
  b, b, c, c, c, c, c, c
]
four = [
  c, c, c, c, c, c, c, c,
  c, b, b, c, c, b, b, c,
  c, b, b, c, c, b, b, c,
  c, c, c, c, c, c, c, c,
  c, c, c, c, c, c, c, c,
  c, b, b, c, c, b, b, c,
  c, b, b, c, c, b, b, c,
  c, c, c, c, c, c, c, c
]
five = [
  c, c, c, c, c, c, c, c,
  c, b, b, c, c, b, b, c,
  c, b, b, c, c, b, b, c,
  c, c, c, b, b, c, c, c,
  c, c, c, b, b, c, c, c,
  c, b, b, c, c, b, b, c,
  c, b, b, c, c, b, b, c,
  c, c, c, c, c, c, c, c
]
six = [
  c, b, b, c, c, b, b, c,
  c, b, b, c, c, b, b, c,
  c, c, c, c, c, c, c, c,
  c, b, b, c, c, b, b, c,
  c, b, b, c, c, b, b, c,
  c, c, c, c, c, c, c, c,
  c, b, b, c, c, b, b, c,
  c, b, b, c, c, b, b, c
]
def roll1(player):
    dice_word = ""
    global list1
    list1 = []
    dice_face = [one, two, three, four, five, six]
    sense.show_message(f"PLAYER {player}, IT IS YOUR TURN!", scroll_speed=0.04, text_colour = (135, 38, 81))
    print(f"Player {player}, press the joystick UP to roll")
    rolled = 0
    while rolled == 0:
        for event in sense.stick.get_events():
            if event.action == "pressed" and event.direction == "up":
                number = randint(1, 6)
                if number == 1:
                    dice_word = one
                if number == 2:
                    dice_word = two
                if number == 3:
                    dice_word = three
                if number == 4:
                    dice_word = four
                if number == 5:
                    dice_word = five
                if number == 6:
                    dice_word = six
                list1 = []
                list1.append(number)
                sense.set_pixels(dice_word)
                sleep(2)
                sense.clear()
                rolled += 1
    if player == 1:
        player = 2
    elif player == 2:
        player =1
    






sense.show_message("WELCOME TO DICE DUEL!", scroll_speed=0.04, text_colour = (135, 38, 81))
sense.show_message("TWO PLAYERS ARE NEEDED. NO MORE, NO LESS.", scroll_speed=0.04, text_colour = (135, 38, 81))


dice_face = [one, two, three, four, five, six]

dice_word = []
word = ""
   
player = 1
player_1_score = 0
player_2_score = 0
game =  0
overall1 = 0
overall2 = 0
while game < 3:
    roll1(1)
    player_2_score = list1.pop()
    overall1 = player_2_score
    roll1(2)
    player_1_score = list1.pop()
    overall2 = player_1_score
    if player_2_score > player_1_score:
        sense.show_message("PLAYER ONE YOU WINNNNN", scroll_speed=0.04, text_colour = (135, 38, 81))
        overall1 = (overall1) + 1
    elif player_1_score > player_2_score:
        sense.show_message("PLAYER TWO YOU WINNNNN", scroll_speed=0.04, text_colour = (135, 38, 81))
        overall2 = 1 + (overall2)
    else:
        sense.show_message("its a tie...", scroll_speed=0.04, text_colour = (135, 38, 81))
    game+= 1
sense.show_message("AND THE WINNER ISSSSS", scroll_speed=0.04, text_colour = (135, 38, 81))
sleep(2)
sense.show_message(".", text_colour = (135, 38, 81))
sleep(2)
sense.show_message(".", text_colour = (135, 38, 81))
sleep(2)
sense.show_message(".", text_colour = (135, 38, 81))
if overall1 > overall2:
    sense.show_message("PLAYER ONE", scroll_speed=0.04, text_colour = (135, 38, 81))
elif overall2 > overall1:
    sense.show_message("PLAYER TWO", scroll_speed=0.04, text_colour = (135, 38, 81))
