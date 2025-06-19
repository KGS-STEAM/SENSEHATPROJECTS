from sense_hat import SenseHat
 
sense = SenseHat()
 
r = (200, 0, 0)
B = (0, 0, 0)
b = (0, 0, 200)
healthdsp1 = [r,r,r,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]
healthdsp2 = [r,r,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]
healthdsp3 = [r,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]
healthdsp4 = [B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]
game_won = False
#player1
sense.show_message("what is the number player two has to guess",scroll_speed=0.05)
thingnumber = int(input())
counter = 3


sense.set_pixels(healthdsp1)


while game_won == False:
#player 2
    print(" what number are you guessing out of 0 - 6 player 2")
    num_taken = int(input())
    if num_taken == thingnumber:
        game_won = True
        sense.show_message("player two has won the game",scroll_speed = 0.05)
    elif counter == 3:
        counter = counter - 1
        sense.set_pixels(healthdsp2)
    elif counter == 2:
        counter = counter - 1
        sense.set_pixels(healthdsp3)
    elif counter == 1:
        counter = counter - 1
        sense.set_pixels(healthdsp4)
        sense.show_message("Player one has won the game",scroll_speed = 0.05)
        game_won = True 
