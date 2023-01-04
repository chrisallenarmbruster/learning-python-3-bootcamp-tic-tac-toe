'''

Tic Tac Toe Game
'''

import random
import os



def choose_xo():
    '''
    Function for beginning of each game to decide who goes first
    '''

    player = ""
    print("\n\n  Starting new game of Tic-Tac-Toe...")
    input(f"\n  Decide who will play as {colorize('X')} and who will play as {colorize('O')} and then press enter when ready: ")
    os.system('clear')
    print("\n\n  Flipping a coin to see who goes first...\n")
    if random.randint(0, 1) == 0:
        #print("  X wins the coin toss and goes first!")
        player = "X"
    else:
        #print("O wins the coin toss and goes first!")
        player = "O"

    input(f"  Player {colorize(player)} won the toss, press enter to begin game: ")

    return player

def colorize(text):
    '''
    Colorizes player moves in the game board
    '''

    if text == "X":
        text = "\033[92;1mX\033[00m"
    elif text == "O":
        text = "\033[91;1mO\033[00m"
    else:
        text = "\033[90m" + str(text) + "\033[00m"
    return text


def print_board(pos_values):
    '''
    Function for printing the game board to the screen
    '''

    os.system('clear')

    print("\n\n       \u2503     \u2503     ")
    print(f"    {colorize(pos_values[1])}  \u2503  {colorize(pos_values[2])}  \u2503  {colorize(pos_values[3])}  ")
    print("       \u2503     \u2503     ")
    print("  \u2501\u2501\u2501\u2501\u2501\u254b\u2501\u2501\u2501\u2501\u2501\u254b\u2501\u2501\u2501\u2501\u2501")
    print("       \u2503     \u2503     ")
    print(f"    {colorize(pos_values[4])}  \u2503  {colorize(pos_values[5])}  \u2503  {colorize(pos_values[6])}  ")
    print("       \u2503     \u2503     ")
    print("  \u2501\u2501\u2501\u2501\u2501\u254b\u2501\u2501\u2501\u2501\u2501\u254b\u2501\u2501\u2501\u2501\u2501")
    print("       \u2503     \u2503     ")
    print(f"    {colorize(pos_values[7])}  \u2503  {colorize(pos_values[8])}  \u2503  {colorize(pos_values[9])}  ")
    print("       \u2503     \u2503     \n\n")

def player_move(pos_values,player):
    '''
    Function to prompt player to make a move
    '''

    legal_moves = [int(x) for x in pos_values if x != "X" and x != "O" and x != "NA"]
    move_legal = False
    while not move_legal:
        move = input(f"  Player {colorize(player)} enter move {legal_moves} ")
        if move.isdigit() and int(move) in legal_moves:
            move_legal = True
        else:
            print_board(pos_values)
            print("  Invalid input! Try again.")
    pos_values[int(move)] = player
    return pos_values


def check_game(pv):
    '''
    Function called after a move is made to determine if there is a winner or tie
    '''

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

    if len([int(x) for x in pv if x not in ('X', 'O', 'NA')]) == 0:
        return "tied"

    return "undetermined"


def activate_game():
    '''
    Main game loop
    '''

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
                print(f"  Player {colorize(player)} wins!\n")
            elif check_game(pos_values) == "tied":
                round_over = True
                print_board(pos_values)
                print("  It's a draw!\n")

            # Change whose turn it is
            if player == "X":
                player = "O"
            else:
                player = "X"

        # Prompt to play again
        if input("  Play again?  Enter Y to continue and anything else to quit: ").upper() != "Y":
            game_active = False


activate_game()
