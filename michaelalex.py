from sense_hat import SenseHat, ACTION_PRESSED, ACTION_RELEASED
from random import randint
from time import sleep
sense = SenseHat()
 
player = 1
player1_points = 0
player2_points = 0
direction_num = 3
 
a_cord = ""
 
list_cords = []
 
length_of_list = len(list_cords)
 
r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 0)
c = (0, 0, 255)
 
x = randint(0, 7)
y = 7
 
   
cord1 = y
cord2 = x
   
 
 
grid = [
    [b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b]
]
 
 
def player_rotation():
  global player
  if player == 1:
    player = 2
  elif player == 2:
    player = 1
   
def check_cords():
  print(list_cords)
  if [y,x] in list_cords:
    print(y,x)
    grid[y][x] = g
    sense.set_pixels(sum(grid, []))
  else:
    wrong()
 
 
 
def cords(y,x):
    list_cords.append([y,x])
 
def right(x):
  if x < 7:
    x += 1
    sleep(0.5)
  return x
 
def left(x):
  if x > 0:
    x -= 1
    sleep(0.5)
  return x
 
def forward(y):
  if y > 0:
    y -= 1
    sleep(0.5)
  return y
 
def wrong():
    grid_wrong = [
        [r, r, r, r, r, r, r, r],
        [r, r, r, r, r, r, r, r],
        [r, r, r, r, r, r, r, r],
        [r, r, r, r, r, r, r, r],
        [r, r, r, r, r, r, r, r],
        [r, r, r, r, r, r, r, r],
        [r, r, r, r, r, r, r, r],
        [r, r, r, r, r, r, r, r]
    ]
    sense.set_pixels(sum(grid_wrong, []))
 
def correct():
    grid_correct = [
        [g, g, g, g, g, g, g, g],
        [g, g, g, g, g, g, g, g],
        [g, g, g, g, g, g, g, g],
        [g, g, g, g, g, g, g, g],
        [g, g, g, g, g, g, g, g],
        [g, g, g, g, g, g, g, g],
        [g, g, g, g, g, g, g, g],
        [g, g, g, g, g, g, g, g]
    ]
    
    sense.set_pixels(sum(grid_correct, []))
    if player == 1:
      player1_points += 1
    elif player == 2:
      player2_points += 1
 
def check_cords():
    print("current",y,x)
    if [y,x] in list_cords:
        grid[y][x] = g
        sense.set_pixels(sum(grid, []))
        if [y,x] == finish:
            sense.clear(g)
            sleep(3)
            sense.clear(b)
            if player == 1:
                player
    else:
        wrong()
 
#Main code
 
print(y,x)
grid[y][x] = c  # y is row, x is column
 
cords(y,x)
 
sense.set_pixels(sum(grid, []))
 
 
 
#the stuff above is movement for when the joystick comes into play and path generation
 
 
 
while y != 0:
  direction = randint(0,2)
  if direction == 0:
    if direction_num != 1:
      x = right(x)
      grid[y][x] = g
      sense.set_pixels(sum(grid, []))
      direction_num = 0
      cords(y,x)
 
  elif direction == 1:
    if direction_num != 0:
      x = left(x)
      grid[y][x] = g
      sense.set_pixels(sum(grid, []))
      direction_num = 1
      cords(y,x)
 
  else:
    y = forward(y)
    grid[y][x] = g
    sense.set_pixels(sum(grid, []))
    direction_num = 3
    cords(y,x)
finish = [y,x]
print("finish",y,x)
 
sleep(3)
 
grid = [
    [b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b]
]
 
grid[cord1][cord2] = c
sense.set_pixels(sum(grid, []))
 
   
 
player_rotation()
 
 
# need to do player 1 or 2 stuff
# need to do a points system
# need to test on a pi
# need to do a green screen if the whole path is correct( reaches the only dot and back line)
# introduction (name, instructions)
 
y = cord1
x = cord2
print("start",y,x)
while True:
    event = sense.stick.wait_for_event(emptybuffer=True)
    #for event in sense.stick.get_events():
    if event.action == ACTION_PRESSED:
        if event.direction == "up":
            y -= 1
            check_cords()
            
             
        elif event.direction == "right":
            x += 1
            check_cords()
            
            
        elif event.direction == "left":
            x -= 1
            check_cords()
    sleep(0.1)
