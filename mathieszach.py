from sense_hat import SenseHat 

from time import sleep 

sense = SenseHat() 

 

y = (255,255,0) 

r = (255,0,0) 

b = (0,0,0) 

move_y = (255,255,0) 

move_r = (255,0,0) 

 

player = "player1" 

 

game = "play" 

 

display = [b,b,b,b,b,b,b,b, 

           b,b,b,b,b,b,b,b, 

           b,b,b,b,b,b,b,b, 

           b,b,b,b,b,b,b,b, 

           b,b,b,b,b,b,b,b, 

           b,b,b,b,b,b,b,b, 

           b,b,b,b,b,b,b,b, 

           b,b,b,b,b,b,b,b 

           ] 

 

move = "no" 

def check_1(a,b): 

    game = "play" 

    for i in range(a,b): 

        if display[i] == y: 

            if display[i+1] == y and display[i+2] == y and display[i+3] == y: 

                game = "stop_y" 

            if i > a+2: 

                if display[i-1] == y and display[i-2] == y and display[i-3] == y: 

                    game = "stop_y" 

                if a < 40: 

                    if display[i+7] == y and display[i+14] == 7 and display[i+21] == y: 

                        game = "stop_y" 

            if a < 40: 

                if display[i+9] == y and display[i+18] == y and display[i+27] == y: 

                    game = "stop_y" 

                if display[i+8] == y and display[i+16] == y and display[i+24] == y: 

                    game = "stop_y" 

        elif display[i] == r: 

            if display[i+1] == r and display[i+2] == r and display[i+3] == r: 

                game = "stop_r" 

            if i > a+2: 

                if display[i-1] == r and display[i-2] == r and display[i-3] == r: 

                    game = "stop_r" 

                if a < 40: 

                    if display[i+7] == r and display[i+14] == r and display[i+21] == r: 

                        game = "stop_r" 

            if a < 40: 

                if display[i+9] == r and display[i+18] == r and display[i+27] == r: 

                    game = "stop_r" 

                if display[i+8] == r and display[i+16] == r and display[i+24] == r: 

                    game = "stop_r" 

    return game 

def check_2(a,b): 

    game = "play" 

    for i in range(a,b): 

        if display[i] ==y: 

            if display[i-1] == y and display[i-2] == y and display[i-3] == y: 

                game = "stop_y" 

            if a < 40: 

                if display[i+7] == y and display[i+14] == y and display[i+21] == y: 

                    game = "stop_y" 

                if display[i+8] == y and display[i+16] == y and display[i+24] == y: 

                    game = "stop_y" 

        elif display[i] == r: 

            if display[i-1] == r and display[i-2] == r and display[i-3] == r: 

                game = "stop_y" 

            if a < 40: 

                if display[i+7] == r and display[i+14] == r and display[i+21] == r: 

                    game = "stop_r" 

                if display[i+8] == r and display[i+16] == r and display[i+24] == r: 

                    game = "stop_r" 

    return game 

         

sense.set_pixels(display) 

 

while game == "play": 

    move = "no" 

    if player == "player1": 

        display.pop(7) 

        display.insert(7,move_r) 

        sense.set_pixels(display) 

    elif player == "player2": 

        display.pop(7) 

        display.insert(7,move_y) 

        sense.set_pixels(display) 

    while move != "yes": 

        for event in sense.stick.get_events(): 

            if event.direction == "left" and event.action == "pressed": 

                for i in range(0,8): 

                    if display[i] == move_y and i > 0: 

                        print("a", i) 

                        display.pop(i) 

                        display.insert(i,b) 

                        display.pop(i-1) 

                        display.insert(i-1, move_y) 

                        sense.set_pixels(display) 

                    elif display[i] == move_r and i > 0: 

                        print("b", i) 

                        display.pop(i) 

                        display.insert(i,b) 

                        display.pop(i-1) 

                        display.insert(i-1, move_r) 

                        sense.set_pixels(display) 

                    elif display[i] == move_y and i == 0: 

                        print("c", i) 

                        display[i] = b 

                        display[7] = move_y 

                        sense.set_pixels(display) 

                        break 

                    elif display[i] == move_r and i == 0: 

                        print("d", i) 

                        display[i] = b 

                        display[7] = move_r 

                        sense.set_pixels(display) 

                        break 

           elif event.action == "pressed" and event.direction == "down": 

                move = "yes" 

    for i in range (0,8): 

        if display[i] == move_y or display[i] == move_r: 

            index_pixel = i 

    while index_pixel < 56 and display[index_pixel+8] != y and display[index_pixel+8] != r: 

        if display[index_pixel] == move_y: 

            display[index_pixel+8] = move_y 

        elif display[index_pixel] == move_r: 

            display[index_pixel + 8] = move_r 

        display[index_pixel] = b 

        sense.set_pixels(display) 

        index_pixel += 8 

        sleep(0.7) 

    for i in range(0,64): 

        if display[i] == move_y: 

            display[i] = y 

        elif display[i] == move_r: 

            display[i] = r 

    game = check_1(0,5) 

    if game == "yes": 

        game = check_2(5,8) 

    if game == "yes": 

        game = check_1(8,13) 

    if game == "yes": 

        game = check_2(13,16) 

    if game == "yes": 

        game = check_1(16,21) 

    if game == "yes": 

        game = check_2(21,24) 

    if game == "yes": 

        game = check_1(24,29) 

    if game == "yes": 

        game = check_2(29,32) 

    if game == "yes": 

        game = check_1(32,37) 

    if game == "yes": 

        game = check_2(37,40) 

    if game == "yes": 

        game = check_1(40,45) 

    if game == "yes": 

        game = check_2(45,48) 

    if game == "yes": 

        game = check_1(48,53) 

    if game == "yes": 

        game = check_2(53,56) 

    if game == "yes": 

        game = check_1(56,61) 

    if game == "yes": 

        game = check_2(61,64) 

     

    if player == "player1": 

        player = "player2" 

    elif player == "player2": 

        player = "player1" 

if game == "stop_y": 

  sense.show_message("Player 2 wins!") 

else: 

  sense.show_message("PLayer 1 wins!") 
