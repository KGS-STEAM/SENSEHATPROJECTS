from sense_hat import SenseHat
from random import choice
from time import sleep
sense = SenseHat()
death_counter=0
red = (255, 0, 0)
blue = (0, 0, 255)
bl = (0, 0, 254) 
blu = (0, 0, 253)
bluu= (0, 0, 249)
b=(0,0,252)
white = (255, 255, 255)
bla = (0, 0, 0)
one = (173,239,25)
bomb=(255,162,0)
grid = [[choice([red, blu, blue, bl,b,bluu]) for _ in range(8)] for _ in range(8)]
gri = [[bla for _ in range(8)] for _ in range(8)]
x, y = 4, 4  
def draw():
    sense.set_pixels(sum(gri, []))
    sense.set_pixel(x, y, white)
def reveal_current_tile():
    gri[y][x] = grid[y][x]
def check_for_red(x, y):
    if grid[y][x] == red:
        sense.show_message("BOOM!", text_colour=red, scroll_speed=0.02)
        gri[y][x]=bomb
        sense.set_pixels(sum(gri, []))
        print("Boom! You stepped on a red tile!")
        return True 
    return False  
def check_for_red_in_area(x, y):
    red_count = 0  
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy 
            if 0 <= nx < 8 and 0 <= ny < 8:
                if grid[ny][nx] == red:
                    red_count += 1
    if red_count == 1:
        color = (245, 0, 0)
    elif red_count == 2:
        color = (255, 0, 100) 
    elif red_count == 3:
        color = (100, 0, 100) 
    elif red_count == 4:
        color = (0, 170, 255) 
    elif red_count == 5:
        color = (0, 255, 157)  
    elif red_count == 6:
        color = (148, 77, 255)  
    elif red_count == 7:
        color = (68, 255, 0) 
    elif red_count == 8:
        color = (238, 255, 0)
    else:
        return
        color = (255,255,255)
    gri[y][x] = color  
    sense.set_pixels(sum(gri, []))
    sense.show_message(str(red_count), text_colour=color, scroll_speed=0.03)
def draw_dot():
    draw()
draw()
while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up" and y > 0:
                y -= 1
            elif event.direction == "down" and y < 7:
                y += 1
            elif event.direction == "left" and x > 0:
                x -= 1
            elif event.direction == "right" and x < 7:
                x += 1
            elif event.direction == "middle":
                if check_for_red(x, y):
                    continue  
                reveal_current_tile()
                check_for_red_in_area(x, y)
            draw()
    sleep(0.05)
