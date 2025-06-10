from sense_hat import SenseHat 

from sense_hat import ACTION_PRESSED, DIRECTION_LEFT, DIRECTION_RIGHT, DIRECTION_MIDDLE 

from time import sleep 

 
 

sense = SenseHat() 

 
 

# colors! 

r = [255, 0, 0] # player 1 

y = [255, 255, 0] # player 2 

e = [0, 0, 0] # empty space 

 
 

# 8 x 8 board 

board = [ 

  e, e, e, e, e, e, e, e, 

  e, e, e, e, e, e, e, e, 

  e, e, e, e, e, e, e, e, 

  e, e, e, e, e, e, e, e, 

  e, e, e, e, e, e, e, e, 

  e, e, e, e, e, e, e, e, 

  e, e, e, e, e, e, e, e, 

  e, e, e, e, e, e, e, e] 

 
 

# display the board 

def display_board(): 

  sense.set_pixels(board) 

   

# let player choose a column 

def choose_column(current_player): 

    column = 3  # Start in the middle 

    selecting = True 

    while selecting: 

        for x in range(8): 

            sense.set_pixel(x, 0, e) 

        if current_player == 1: 

            sense.set_pixel(column, 0, r) 

        else: 

            sense.set_pixel(column, 0, y) 

        for event in sense.stick.get_events(): 

            if event.action == ACTION_PRESSED: 

                if event.direction == DIRECTION_LEFT and column > 0: 

                    column -= 1 

                elif event.direction == DIRECTION_RIGHT and column < 7: 

                    column += 1 

                elif event.direction == DIRECTION_MIDDLE: 

                    selecting = False 

        sleep(0.1) 

    return column 

# --- Drop a chip in the chosen column --- 

def drop_chip(column, current_player): 

    for row in range(7, 0, -1): 

 
 

        if board[row][column] == e: 

 
 

            if current_player == 1: 

 
 

                board[row][column] = r 

 
 

            else: 

 
 

                board[row][column] = y 

 
 

            return True 

 
 

    return False  # Column is full 

 
 

 
 

 
 

# --- Check if a player has won --- 

 
 

def check_win(color): 

 
 

    # Check rows 

 
 

    for row in range(8): 

 
 

        for col in range(5): 

 
 

            if board[row][col] == color and board[row][col+1] == color and board[row][col+2] == color and board[row][col+3] == color: 

 
 

                return True 

 
 

 
 

 
 

    # Check columns 

 
 

    for col in range(8): 

 
 

        for row in range(5): 

 
 

            if board[row][col] == color and board[row+1][col] == color and board[row+2][col] == color and board[row+3][col] == color: 

 
 

                return True 

 
 

 
 

 
 

    # Check diagonals ↘ 

 
 

    for row in range(5): 

 
 

        for col in range(5): 

 
 

            if board[row][col] == color and board[row+1][col+1] == color and board[row+2][col+2] == color and board[row+3][col+3] == color: 

 
 

                return True 

 
 

 
 

 
 

    # Check diagonals ↙ 

 
 

    for row in range(5): 

 
 

        for col in range(3, 8): 

 
 

            if board[row][col] == color and board[row+1][col-1] == color and board[row+2][col-2] == color and board[row+3][col-3] == color: 

 
 

                return True 

 
 

 
 

 
 

    return False 

 
 

 
 

 
 

# --- Main game function --- 

 
 

def play_game(): 

 
 

    current_player = 1 

 
 

    winner = False 

 
 

 
 

 
 

    while not winner: 

 
 

        display_board() 

 
 

 
 

 
 

        column = choose_column(current_player) 

 
 

        dropped = drop_chip(column, current_player) 

 
 

 
 

 
 

        if dropped: 

 
 

            display_board() 

 
 

            if current_player == 1: 

 
 

                color = r 

 
 

            else: 

 
 

                color = y 

 
 

 
 

 
 

            if check_win(color): 

 
 

                winner = True 

 
 

                sense.show_message("P" + str(current_player) + " wins!") 

 
 

            else: 

 
 

                current_player = 2 if current_player == 1 else 1 

 
 

        else: 

 
 

            sense.show_message("Full!") 

 
 

 
 

 
 

# --- Start the game --- 

 
 

play_game() 
