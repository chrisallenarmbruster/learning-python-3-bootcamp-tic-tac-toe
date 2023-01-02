import random
import os


# Function for beginning of each game to decide who goes first
def choose_xo():
    print(" ")
    print(" ")
    print("  Starting new game of Tic-Tac-Toe...")
    print(" ")
    input("  Decide who will play as X and who will play as O and then press enter when ready: ")
    print("")
    print("  Flipping a coin to see who goes first.")
    print("")
    if random.randint(0, 1) == 0:
        print("  X wins the coin toss and goes first!")
        return "X"
    else:
        print("O wins the coin toss and goes first!")
        return "O"

# Colorizes player moves in the game board
def colorize(text):
    if text == "X":
        text = "\033[92;1mX\033[00m"
    elif text == "O":
        text = "\033[91;1mO\033[00m"
    else:
        text = "\033[90m" + str(text) + "\033[00m" 
    return text


# Function for printing the game board to the screen
def print_board(pos_values):
    os.system('clear')
    print(" ")
    print(" ")
    print("       |     |     ")
    print(f"    {colorize(pos_values[1])}  |  {colorize(pos_values[2])}  |  {colorize(pos_values[3])}  ")
    print("       |     |     ")
    print("  -----------------")
    print("       |     |     ")
    print(f"    {colorize(pos_values[4])}  |  {colorize(pos_values[5])}  |  {colorize(pos_values[6])}  ")
    print("       |     |     ")
    print("  -----------------")
    print("       |     |     ")
    print(f"    {colorize(pos_values[7])}  |  {colorize(pos_values[8])}  |  {colorize(pos_values[9])}  ")
    print("       |     |     ")
    print(" ")
    print(" ")
    

# Function to prompt player to make a move
def player_move(pos_values,player):
    legal_moves = [int(x) for x in pos_values if x != "X" and x != "O" and x != "NA"]
    move_legal = False
    while not move_legal:
        move = input(f"  Player {player} enter move {legal_moves} ")
        if move.isdigit() and int(move) in legal_moves:
            move_legal = True
        else:
            print_board(pos_values)
            print("  Invalid input! Try again.")
    pos_values[int(move)] = player
    return pos_values   


# Function called after a move is made to determine if there is a winner or tie
def check_game(pv):
    if (
        pv[1] == pv[2] == pv[3] or 
        pv[4] == pv[5] == pv[6] or
        pv[7] == pv[8] == pv[9] or
        pv[1] == pv[4] == pv[7] or
        pv[2] == pv[5] == pv[8] or
        pv[3] == pv[6] == pv[9] or
        pv[1] == pv[5] == pv[9] or
        pv[3] == pv[5] == pv[7]
    ):
        return "winner"

    elif len([int(x) for x in pv if x != "X" and x != "O" and x != "NA"]) == 0:
        return "tied"
    else:
        return "undetermined"


# Main game loop
def activate_game():
    game_active = True
    
    while game_active:
        round_over = False

        # List to hold status of the game board, index 0 not used
        pos_values=["NA","1","2","3","4","5","6","7","8","9"]
        
        os.system('clear')

        player = choose_xo()
        
        while not round_over:
            # Print game board
            print_board(pos_values)

            # Get player move
            pos_values = player_move(pos_values,player)

            # Check status afer move (Is there a winner or tie?)
            if check_game(pos_values) == "winner":
                round_over = True
                print_board(pos_values)
                print(f"  Player {player} wins!")
                print(" ")
            elif check_game(pos_values) == "tied":
                round_over = True
                print_board(pos_values)
                print("  It's a draw!")
                print(" ")

            # Change whose turn it is
            if player == "X":
                player = "O"
            else:
                player = "X"

        # Prompt to play again
        if input("  Play again?  Enter Y to continue and anything else to quit: ").upper() != "Y":
            game_active = False

        print(" ")

activate_game()