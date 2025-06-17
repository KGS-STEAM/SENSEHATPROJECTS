 

from sense_hat import SenseHat 

import time 

import random 

sense = SenseHat() 

sense.clear() 

#Clours 

BIRD = (0,255,0) 

PIPE = (255,0,0) 

 
 

#BIRD settings 

bird_x = 1 

bird_y = 4 

 
 

velocity = 0 

 
 

gravity = 0.25 

 
 

flap_strength = -1.0 

 
 

# Game settings 

pipes  = [] 

pipe_speed = 0.3 

pipe_interval = 8 

gap_size = 2 

frame = 0 

game_over = False 

 
 

start_time = time.time() 

 
 

# Joystick: Flap when UP is pressed 

def flap(event): 

    global velocity 

    if event.action == "pressed": 

        velocity = flap_strength 

         

sense.stick.direction_up = flap 

 
 

# Add a new pipe with valid gap 

def add_pipe(): 

    max_top = 8 - gap_size - 1 # 7 - 2 = 5 

    gap_y = random.randint(1, max_top) # random: can be 1, 2, 3 or 4, for example 3 (GAP_Y IS THE Y COORD OF THE TOP OF THE GAP) 

    pipes.append({"x": 7, "gap-y": gap_y}) # for example "x": 7, "gap-y": 3 

    print(f"gap_y = {gap_y}") 

     

# Draw bird and pipes 

def draw(): 

    sense.clear() 

    #Draw bird 

    if 0 <= int(bird_y) < 8: 

        sense.set_pixel(bird_x, int(bird_y), BIRD) 

 
 

# Draw pipes 

    for pipe in pipes: 

        x = pipe["x"] # x = 7 

        gap_y = pipe["gap-y"] # fo('Cannot detect %s device' % self.SENSE_HAT_FB_NAME) 

 
 

         

        for y in range(8): 

            if y < gap_y or y >= gap_y + gap_size: # for example: smaller than 3 or greater or equal to 5: (0, 1, 2), (5,6,7) 

                if 0 <= x < 8: 

                    sense.set_pixel(x, y, PIPE) 

     

                     

# Start game 

# add_pipe() 

 
 

scores = [0, 0] 

player = 1 

 
 

sense.show_message("Player 1 turn", text_colour=(0, 255, 0)) 

 
 

 
 

try: 

     

    for i in range(2): 

 
 

        while not game_over: 

             

            current_time = time.time() 

            elapsed = current_time - start_time 

             

            score = elapsed 

             

            # Add pipe every interval 

            if frame % pipe_interval == 0: 

                add_pipe() 

                 

                 

            # Move pipes left 

            for pipe in pipes: 

                pipe["x"] -= 1 

                 

            pipes = [pipe for pipe in pipes if pipe["x"] >= 0] 

             

            #Apply gravity 

            velocity += gravity 

            bird_y += velocity 

             

            #Check for collisions 

            for pipe in pipes: 

                if pipe["x"] == bird_x: 

                    if int(bird_y) < pipe["gap-y"] or int(bird_y) >= pipe["gap-y"] + gap_size: 

                        game_over = True 

                        if player == 1: 

                            scores[0] = score 

                        elif player == 2: 

                            scores[1] = score 

                         

            #Out of bounds 

            if bird_y < 0 or bird_y >= 8: 

                game_over = True 

             

             

            draw() 

            time.sleep(pipe_speed) 

            frame+=1 

             

            #Game over 

            if game_over: 

                sense.show_message("Game over", text_colour=(255, 0, 0)) 

                sense.clear() 

                 

        if player == 1: sense.show_message("Player 2 turn", text_colour=(0, 255, 0)) 

             

        game_over = False 

        player = 2 

        pipes = [] 

        bird_x = 1 

        bird_y = 4 

        velocity = 0 

        start_time = time.time() 

    

 
 

   

   

   

   

except KeyboardInterrupt: 

  

 sense.clear() 

     

     

     

if scores[0] > scores[1]: # player 1 is winner 

    sense.show_message(f"Player 1 is winner, with score of {int(scores[0])}", text_colour=(0, 255, 0)) 

elif scores[0] < scores[1]: # player 2 is winner 

    sense.show_message(f"Player 2 is winner, with score of {int(scores[1])}", text_colour=(0, 255, 0)) 

else: 

    sense.show_message(f"Draw, with score of {scores[1]}", text_colour=(0, 255, 0)) 

 
 

 

 

 
