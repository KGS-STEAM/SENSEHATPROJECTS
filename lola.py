from sense_hat import SenseHat 

sense = SenseHat() 

# Colours 

C = (0, 0, 255)   # Grid lines 

G = (0, 255, 0)   # Player 1 

R = (255, 0, 0)   # Player 2 

B = (0, 0, 0)     # Blank 

# Initial board with grid lines 

board = [ 

  B, B, C, B, B, C, B, B, 

  B, B, C, B, B, C, B, B, 

  C, C, C, C, C, C, C, C, 

  B, B, C, B, B, C, B, B, 

  B, B, C, B, B, C, B, B, 

  C, C, C, C, C, C, C, C, 

  B, B, C, B, B, C, B, B, 

  B, B, C, B, B, C, B, B, 

] 

sense.set_pixels(board) 

# Win check function 

def check_win(colour): 

    win_combos = [ 

        # Rows 

        [0, 1, 3, 4, 6, 7], 

        [24, 25, 27, 28, 30, 31], 

        [48, 49, 51, 52, 54, 55], 

        # Columns 

        [0, 1, 24, 25, 48, 49], 

        [3, 4, 27, 28, 51, 52], 

        [6, 7, 30, 31, 54, 55], 

        # Diagonals 

        [0, 1, 27, 28, 54, 55], 

        [6, 7, 27, 28, 48, 49], 

    ] 

    for combo in win_combos: 

        if all(board[i] == colour for i in combo): 

            return True 

    return False 

# Game loop 

turn = 0 

while turn < 9: 

    if turn % 2 == 0: 

      player = 1 

    else: 

      player = 2 

    if player == 1: 

      colour = G 

    else: 

      colour = R 

    print("Player {player}, where would you like to move?") 

    move = input().lower() 

    if move == "top left": 

        board[0] = colour 

        board[1] = colour 

        board[8] = colour 

        board[9] = colour 

        

    elif move == "top middle": 

        board[3] = colour 

        board[4] = colour 

        board[11] = colour 

        board[12] = colour 

        

    elif move == "top right": 

        board[6] = colour 

        board[7] = colour 

        board[14] = colour 

        board[15] = colour 

        

    elif move == "middle left": 

        board[24] = colour 

        board[25] = colour 

        board[32] = colour 

        board[33] = colour 

        

    elif move == "center" or move == "middle": 

        board[27] = colour 

        board[28] = colour 

        board[35] = colour 

        board[36] = colour 

        

    elif move == "middle right": 

        board[30] = colour 

        board[31] = colour 

        board[38] = colour 

        board[39] = colour 

        

    elif move == "bottom left": 

        board[48] = colour 

        board[49] = colour 

        board[56] = colour 

        board[57] = colour 

        

    elif move == "bottom middle": 

        board[51] = colour 

        board[52] = colour 

        board[59] = colour 

        board[60] = colour 

        

    elif move == "bottom right": 

        board[54] = colour 

        board[55] = colour 

        board[62] = colour 

        board[63] = colour 

        

    else: 

        print("Invalid move, try again.") 

        continue 

    sense.set_pixels(board) 

    if check_win(colour): 

        print("Player {player} wins!") 

        sense.show_message("Player {player} wins!", text_colour=colour) 

        break 

    turn += 1 

if turn == 9: 

    print("It's a draw!") 

    sense.show_message("Draw!", text_colour=(255, 255, 0)) 
