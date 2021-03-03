# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html. 

# TODOs:  
# 1. Find all TODO items and see whether you can improve the code. 
#    In most cases (if not all), you can make them more readable/modular.
# 2. Add/fix function's docstrings (use """ insted of # for function's header
#    comments)

import random

def draw_board(board):
    # This function prints out the board that it was passed.
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def input_player_letter():
    """ Lets the player type which letter they want to be.
    Returns a list with the player’s letter as the first item, and the computer's letter as the second."""
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:                       
        return ['O', 'X']

def who_goes_first():
    """ Randomly choose the player who goes first."""
    if random.randint(0, 1) == 0:
        return 'computer'
    else:                       
        return 'player'

def play_again():
    """ This function returns True if the player wants to play again, otherwise it returns False."""
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def make_move(board, letter, move):
    board[move] = letter

def is_winner(bo, le):
    """ Given a board and a player’s letter, this function returns True if that player has won.
    We use bo instead of board and le instead of letter so we don’t have to type as much."""
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle    # Fix the indentation of this lines and the following ones.
            (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom    # Added indentation to line up the lines of code for easy reading.
            (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def get_board_copy(board):
    """Make a duplicate of the board list and return it the duplicate."""
    dupeBoard = []
    board_length = len(board)
    # changed i to a different name that can be understood
    for value in range(board_length): # Range will start at 0 by default. Clean this mess!
        dupeBoard.append(board[value])

    return dupeBoard

def is_space_free(board, move):
    """Return true if the passed move is free on the passed board."""
    return board[move] == ' '

def get_player_move(board):
    """Let the player type in their move."""
    player_move = ' ' # W0621: Redefining name 'move' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
    # Changed variable name to "player_move"
    while player_move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(player_move)):
        print('What is your next move? (1-9)')
        player_move = input()
    return int(player_move)

def choose_random_move_from_list(board, movesList):
    """Returns a valid move from the passed list on the passed board.
    Returns None if there is no valid move."""
    possibleMoves = []
    for move in movesList:
        if is_space_free(board, move):
            possibleMoves.append(move)

    if len(possibleMoves) != 0: # How would you write this pythanically? (You can google for it!)
        return random.choice(possibleMoves)
    # Else is not needed since the if statement will either pass first, return, and exit the function
    # before returning None
    return None

def get_computer_move(board, comp_letter): # W0621: Redefining name 'computerLetter' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
    """Given a board and the computer's letter, determine where to move and return that move."""
    # Redefined computerLetter to comp_letter
    if comp_letter == 'X':
        play_letter = 'O'
    else:
        play_letter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, board_size):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, comp_letter, i)
            if is_winner(copy, comp_letter):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, board_size):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, play_letter, i)
            if is_winner(copy, play_letter):
                return i

    # Try to take one of the corners, if they are free.
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move is not None: # Fix it (Hint: Comparisons to singletons like None should always be done with is or is not, never the equality/inequality operators.)
        return move

    # Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5

    # Move on one of the sides.
    return choose_random_move_from_list(board, [2, 4, 6, 8])

def is_board_full(board):
    """Return True if every space on the board has been taken. Otherwise return False."""
    for i in range(1, board_size):
        if is_space_free(board, i):
            return False
    return True

# NEW FUNCTIONS ADDED TO REFACTOR CODE BLOCK BELOW
def is_game_playing(given_turn, given_board, given_play_letter, given_comp_letter):
    """See whether the game is playing by:
        Checking if there is a winner,
        Check whether there is a tie"""
    player_has_won = is_winner(given_board, given_play_letter)
    computer_has_won = is_winner(given_board, given_comp_letter)
    tie_game = is_board_full(given_board)

    # Check if there is a winner, the game would end if there is one
    # if either of the players is_winner returns true, the game has ended due to a winner
    if player_has_won or computer_has_won:
        draw_board(given_board)
        if given_turn == 'player': 
            print('Hooray! You have won the game!') # If its the player's turn
        else:
            print('The computer has beaten you! You Lose.') # If its the computer's turn
        return False

    if tie_game:
        # There is a tie so the game will end
        draw_board(given_board)
        print('The game is a tie!')
        return False
        
    return True

def player_turn(play_board, play_letter, comp_letter):
    """Get the player's move and make the changes to the board"""
    draw_board(play_board)
    play_move = get_player_move(play_board)
    make_move(play_board, play_letter, play_move)

def computer_turn(comp_board, play_letter, comp_letter):
    """Get the computer's move and make the changes to the board"""
    comp_move = get_computer_move(comp_board, comp_letter)
    make_move(comp_board, comp_letter, comp_move)

print('Welcome to Tic Tac Toe!')

# The following mega code block is a huge hairy monster. Break it down 
# into smaller methods. Use TODO s and the comment above each section as a guide 
# for refactoring.

while True:
    # Reset the board
    board_size = 10
    # Stored 10 inside of board_size
    the_board = [' '] * board_size # Refactor the magic number in this line (and all of the occurrences of 10 thare are conceptually the same.)
    player_letter, computer_letter = input_player_letter()
    turn = who_goes_first()
    print('The ' + turn + ' will go first.')

    while True: # Usually (not always), loops (or their content) are good candidates to be extracted into their own function.
    #             Use a meaningful name for the function you choose.
        # Player’s turn.
        if turn == 'player':
            player_turn(the_board, player_letter, computer_letter)

            if is_game_playing(turn, the_board, player_letter, computer_letter):
                turn = 'computer'
            else:
                break

        # Computer’s turn.
        else:
            computer_turn(the_board, player_letter, computer_letter)

            if is_game_playing(turn, the_board, player_letter, computer_letter):
                turn = 'player'
            else:
                break
    if not play_again():
        break