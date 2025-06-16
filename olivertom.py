from sense_hat import SenseHat
sense = SenseHat()

R = (255, 0, 0)
Y = (255, 255, 0)
B = (0, 0, 0)
board = [[B,B,B,B,B,B,B,B],
         [B,B,B,B,B,B,B,B],
         [B,B,B,B,B,B,B,B],
         [B,B,B,B,B,B,B,B],
         [B,B,B,B,B,B,B,B],
         [B,B,B,B,B,B,B,B],
         [B,B,B,B,B,B,B,B],
         [B,B,B,B,B,B,B,B]
         ]

sense.set_pixels(sum(board,[]))
game_over = False
player = 2
while game_over == False:
    if player == 2:
        player = 1
    else:
        player = 2
    column = int(input(f"player {player} input the column (1 - 8) that you want to slot your counter in"))
    while column > 8 or column < 1:
        print("You need to enter a number from 1 - 8")
        column = int(input(f"player {player} input the column (1 - 8) that you want to slot your counter in"))
    
    if player == 1:
        
        for i in range(7,0,-1):
            if board[i][column - 1] == B:
                board[i][column - 1 = R
                break
                
        sense.set_pixels(sum(board,[]))
        
        
    elif player == 2:
        
        for i in range(7,0,-1):
            if board[i][column - 1] == B:
                board[i][column - 1 = Y
                break
                
        sense.set_pixels(sum(board,[]))
