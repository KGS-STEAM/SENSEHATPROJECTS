from sense_hat import SenseHat 

sense = SenseHat() 

 
 

b = (0, 0, 255) 

c = (0, 0, 0) 

 
 

sense.show_message = ("Welcome to Connect 4.") 

 
 

 
 

background = [ 

    b, c, c, c, c, c, c, b, 

    b, c, c, c, c, c, c, b, 

    b, c, c, c, c, c, c, b, 

    b, c, c, c, c, c, c, b, 

    b, c, c, c, c, c, c, b, 

    b, c, c, c, c, c, c, b, 

    b, c, c, c, c, c, c, b, 

    b, b, b, b, b, b, b, b, 

    ] 

                     

 
 

sense.set_pixels(background) 

r = (255, 0, 0) 

y = (255, 255, 0) 

while True: 

    coordinate_1 = 4 

    coordinate_2 = 0 

    sense.set_pixel(4, 0, r) 

    pressed = True 

    pressed2 = False 

    while pressed == True: 

            for event in sense.stick.get_events(): 

                print(event.direction, event.action) 

                if event.action == "pressed": 

                     

                    if event.direction == "up": 

                        if coordinate_2 > -1 and coordinate_2 < 6:  

                            sense.set_pixel(coordinate_1, coordinate_2, c) 

                            coordinate_2 -= 1 

                            sense.set_pixel(coordinate_1, coordinate_2, r) 

                    elif event.direction == "down": 

                        if coordinate_2 > -1 and coordinate_2 < 6:  

                            sense.set_pixel(coordinate_1, coordinate_2, c) 

                            coordinate_2 += 1 

                            sense.set_pixel(coordinate_1, coordinate_2, r) 

                    elif event.direction == "left": 

                        if coordinate_1 > 1 and coordinate_1 < 6:  

                            sense.set_pixel(coordinate_1, coordinate_2, c) 

                            coordinate_1 -= 1 

                            sense.set_pixel(coordinate_1, coordinate_2, r) 

                    elif event.direction == "right": 

                        if coordinate_1 > 1 and coordinate_1 < 6:  

                            sense.set_pixel(coordinate_1, coordinate_2, c) 

                            coordinate_1 += 1 

                            sense.set_pixel(coordinate_1, coordinate_2, r) 

                    elif event.direction == "middle": 

                        pressed = False 

                        sense.set_pixel(coordinate_1, coordinate_2, r) 

                        #sense.set_pixel(coordinate_1, coordinate_2, c) 

                        #coordinate_1 += 1 

                        #sense.set_pixel(coordinate_1, coordinate_2, r) 

    coordinate_1 = 4 

    coordinate_2 = 0 

    sense.set_pixel(4, 0, y) 

    while pressed2 == False: 

             for event in sense.stick.get_events(): 

                print(event.direction, event.action) 

                if event.action == "pressed": 

                         

                        if event.direction == "up": 

                            if coordinate_2 > -1 and coordinate_2 < 6:  

                                sense.set_pixel(coordinate_1, coordinate_2, c) 

                                coordinate_2 -= 1 

                                sense.set_pixel(coordinate_1, coordinate_2, y) 

                        elif event.direction == "down": 

                            if coordinate_2 > -1 and coordinate_2 < 6:  

                                sense.set_pixel(coordinate_1, coordinate_2, c) 

                                coordinate_2 += 1 

                                sense.set_pixel(coordinate_1, coordinate_2, y) 

                        elif event.direction == "left": 

                            if coordinate_1 > 1 and coordinate_1 < 6:  

                                sense.set_pixel(coordinate_1, coordinate_2, c) 

                                coordinate_1 -= 1 

                                sense.set_pixel(coordinate_1, coordinate_2, y) 

                        elif event.direction == "right": 

                            if coordinate_1 > 1 and coordinate_1 < 6:  

                                sense.set_pixe 

                                l(coordinate_1, coordinate_2, c) 

                                coordinate_1 += 1 

                                sense.set_pixel(coordinate_1, coordinate_2, y) 

                        elif event.direction == "middle": 

                            pressed2 = True 

                            sense.set_pixel(coordinate_1, coordinate_2, y) 
