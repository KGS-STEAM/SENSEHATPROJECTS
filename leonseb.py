from sense_hat import SenseHat


from time import sleep


from random import randint, choice


sense = SenseHat()


sense.show_message("welcome to colour clash! you will compete with a friend and in this game. each round you will have to repeat the colour sequence back and you will get a mark out of 6. good luck!", scroll_speed = 0.07)
sleep(2)
sense.show_message("You and your friend must decide who is player 1 and who is player 2", scroll_speed = 0.07)
sleep(2)


R = (255, 0, 0)
G = (0, 255, 0)
B = (0, 0, 255)
O = (255, 128, 0)
Y = (255, 255, 0)
P = (191, 0, 255)
W = (0, 0, 0)






a_list = [B, R, G, O, Y, P]
colours = []




if answer =="R":
    answer = (255, 0, 0)
if answer =="B":
    answer = (0, 0, 255)
if answer =="G":
    answer = (0, 255, 0)
if answer =="O":
    answer = (255, 128, 0)
if answer =="Y":
    answer = (255, 255, 0)
if answer =="P":
    answer = (191, 0, 255)
sense.show_message("Is player 1 at the computer?", scroll_speed = 0.07)
player_1 = input().lower()


while player1_ready != "yes":
    sense.show_message("Waiting for player 1...", scroll_speed = 0.07)
    player1_ready = input("Is player 1 at the computer? (yes or no): ").lower()
points = 0
num_attempts = 3
while num_attempts > 0:
 
    for i in range(6):


        colours.append(choice(a_list))
   
    for colour in colours:
        sense.clear(colour)
        sleep(1)
        sense.clear(W)
        sleep(1)
   
    guesses = []
    sense.show_message("please type in your answer by typing the letter of the colour and entering. For example: R", scroll_speed = 0.07)
    answer1 = input().lower()
    guesses.append(answer1)


    answer2 = input().lower()
    guesses.append(answer2)
   
    answer3 = input().lower()
    guesses.append(answer3)
   
    answer4 = input().lower()
    guesses.append(answer4)


    answer5 = input().lower()
    guesses.append(answer5)


    answer6 = input().lower()
    guesses.append(answer6)
   
    if guesses == colours:
        sense.show_message("Correct! well done!")
        points = points +1
        num_attempts = num_attempts - 1
    else:
        sense.show_message("Incorrect. You lose!")
        num_attempts = num_attempts - 1
sense.show_message("you scored {} out of 3".format(points), scroll_speed = 0.07)


sleep(2)


sense.show_message("Is player 2 at the computer?", scroll_speed = 0.07)
player_2 = input().lower()


while player2_ready != "yes":
    sense.show_message("Waiting for player 2...", scroll_speed = 0.07)
    player2_ready = input("Is player 2 at the computer? (yes or no): ").lower()
    points2 = 0
    num_attempts2 = 3
    while num_attempts2 > 0:
 
        for i in range(6):


        colours.append(choice(a_list))
   
        for colour in colours:
        sense.clear(colour)
        sleep(1)
        sense.clear(W)
        sleep(1)
   
        guesses = []
        sense.show_message("please type in your answer by typing the letter of the colour and entering. For example: R", scroll_speed = 0.07)
        answer1 = input().lower()
        guesses.append(answer1)


        answer2 = input().lower()
        guesses.append(answer2)
     
        answer3 = input().lower()
        guesses.append(answer3)
     
        answer4 = input().lower()
        guesses.append(answer4)


        answer5 = input().lower()
        guesses.append(answer5)


        answer6 = input().lower()
        guesses.append(answer6)
     
        if guesses == colours:
          sense.show_message("Correct! well done!")
          points2 = points2 +1
          num_attempts2 = num_attempts2 - 1
        else:
         sense.show_message("Incorrect. You lose!")
         num_attempts2 = num_attempts2 - 1
sense.show_message("you scored {} out of 3".format(points2), scroll_speed = 0.07)
if points2 > points:
    sense.show_message("Player 2 wins", scroll_speed = 0.07)
elif points > points2:
    sense.show_message("player 1 wins", scroll_speed = 0.07)
else:
    sense.show_message("It is a draw", scroll_speed = 0.07)
