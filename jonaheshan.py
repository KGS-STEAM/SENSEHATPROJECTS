from sense_hat import SenseHat
import random
from time import sleep
s = SenseHat()



bomb_count = 7 # start num of bomsb
s.clear()

game_over = False

score = 0

g = (0,255,0) # P1
r = (255,0,0) # bomb color
yellow = (255,255,0) # goal colour
w = (0,0,255) # wall colour
p2 = (128,0,128) # p2

wall_layout_2 = [(7,0), (6,0), (7,1), (4,4), (5,4), (6,4), (7,4),(0,7),(0,6)]
wall_layout_3 = [(6,0), (5,0), (4,0), (3,0), (7,0), (0,4), (0,5), (0,6), (3,3), (4,3), (5,3), (5,5), (6,5)]
wall_layout_4 = [(7,0), (6,0), (5,0), (4,0), (3,0),(3,4),(3,5),(3,6),(4,4), (5,4)]
wall_layout_5 = [(5,2), (7,5), (6,5), (5,5),(4,5),(3,5),(2,5),(3,2),(2,2),(1,2),(0,2),(4,2)]
wall_layout_6 = [(7,0), (6,0), (5,0), (4,0), (3,0), (0,6), (0,7), (3,5), (4,5), (5,5), (3,4),(4,4),(5,4),(3,3),(4,3),(5,3)]

wall_class = [wall_layout_3,wall_layout_4,wall_layout_5,wall_layout_6,wall_layout_2]
wall_select = random.choice(wall_class)
for wx3,wy3 in wall_select:
  s.set_pixel(wx3,wy3,w)



 # build up all the walls
colour_of_character = p2
for wx, wy in wall_select:
  s.set_pixel(wx, wy, w)

  
def movement():
  global win,y,x,score,game_over
  while True:
      for event in s.stick.get_events():
          if event.action == "pressed":
              if event.direction == "up":
                  new_y = max(0, y - 1)
                  if (x, new_y) not in wall_select:
                      y = new_y
              elif event.direction == "down":
                  new_y = min(7, y + 1)
                  if (x, new_y) not in wall_select:
                      y = new_y
              elif event.direction == "left":
                  new_x = max(0, x - 1)
                  if (new_x, y) not in wall_select:
                      x = new_x
              elif event.direction == "right":
                  new_x = min(7, x + 1)
                  if (new_x, y) not in wall_select:
                      x = new_x
  
              if (x, y) in bombs:
                  
                  game_over = True
              elif (x, y) == (x2, y2):
                  
                  win = True
              else:
                  score += 1
                  
  
              s.clear()
              for wx, wy in wall_select:
                  s.set_pixel(wx, wy, w)
              s.set_pixel(x, y, colour_of_character)
              s.set_pixel(x2, y2, yellow)
  
      sleep(0.01)
      if win:
          break
      if game_over == True:
        break
      
      
def flash():
    for i in range(5):
        sleep(0.5)
        for bx, by in bombs:
             s.set_pixel(bx, by, r)
        sleep(0.5)
        s.clear()
        for wx, wy in wall_select:
            s.set_pixel(wx, wy, w)
        s.set_pixel(x, y, colour_of_character )
        s.set_pixel(x2, y2, yellow)
    s.set_pixel(x, y, colour_of_character)

      
      

while True: # inf loop 
  
  colour_of_character = g
  bomb_count = bomb_count +1
  win = False
  game_over = False
  
  
 x = 7
 y = 7,  # start cords of player
 x2 = 0
 y2 = 0  # cords of the goal
  
  s.set_pixel(x, y, g)
  s.set_pixel(x2, y2, yellow)
  
  x = 7
  y = 7

  bombs = []
  while len(bombs) < bomb_count:
      bx, by = random.randint(0, 7), random.randint(0, 7)
      if (bx, by) not in bombs and (bx, by) != (x, y) and (bx, by) != (x2, y2) and (bx, by) not in wall_select:
          if (bx + 1,by) not in bombs and (bx - 1,by) not in bombs:
            if (bx,by+1) not in bombs and (bx,by - 1) not in bombs:
              if(bx + 1,by + 1) not in bombs and (bx - 1,by - 1) not in bombs:
                if (bx - 1,by+1) not in bombs and (bx + 1,by - 1) not in bombs:
                  bombs.append((bx, by))
  for bx, by in bombs:
    s.set_pixel(bx, by, r)
  
    
    
  for wx, wy in wall_select:
    s.set_pixel(wx, wy, w)
  
  flash()
  
  
  movement()
  
  flash()
  s.clear()
  
  if game_over:  
    s.show_message("Game Over" + str(score))
    break
    
  if win: 
    s.show_message("Level " + str(bomb_count - 7) + " Passed P1")
    
  colour_of_character = g
  sleep(4)
  win = False
  x = 7
  y = 7
  x2 =  0
  Y2 = 0
  
  new_x = x
  new_y = y
  s.set_pixel(x,y,p2)
  
  bombs = []
  while len(bombs) < bomb_count:
      bx, by = random.randint(0, 7), random.randint(0, 7)
      if (bx, by) not in bombs and (bx, by) != (x, y) and (bx, by) != (x2, y2) and (bx, by) not in wall_select:
          if (bx + 1,by) not in bombs and (bx - 1,by) not in bombs:
            if (bx,by+1) not in bombs and (bx,by - 1) not in bombs:
              if(bx + 1,by + 1) not in bombs and (bx - 1,by - 1) not in bombs:
                if (bx - 1,by+1) not in bombs and (bx + 1,by - 1) not in bombs:
                  bombs.append((bx, by))
  for bx, by in bombs:
              s.set_pixel(bx, by, r)
  
  
  colour_of_character = p2
  
  flash()
  
  movement()
  
  
  
  flash()
  s.clear()
  s.show_message("Level " + str(bomb_count - 7) + " Passed P2") 
  wall_select = random.choice(wall_class)
    
