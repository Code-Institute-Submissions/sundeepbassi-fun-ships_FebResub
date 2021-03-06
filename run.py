import random
import re
# The code for this file is accredited to:
# Knowledge Mavens2(https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.  # noqa: E501

# These variables show the symbols for the player and computer

playerLetter = 'X'
computerLetter = 'O'

# This function will define the board
board = [' ' for i in range(10)]


# This function will add a print of the grid board
def print_board():
    """ print board docstring """
    print('#########################')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('----------')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('----------')
    print(board[7] + '|' + board[8] + '|' + board[9])


# This function will check if the  board is full
def is_full():
    """ is full docstring """
    return ' ' not in board[1:10]


# check if there is a winner
def check_win(board, letter):
    """ check win docstring """
    return (board[1] == board[2] == board[3] == letter) or \
        (board[4] == board[5] == board[6] == letter) or \
        (board[7] == board[8] == board[9] == letter) or \
        (board[1] == board[4] == board[7] == letter) or \
        (board[2] == board[5] == board[8] == letter) or \
        (board[3] == board[6] == board[9] == letter) or \
        (board[1] == board[5] == board[9] == letter) or \
        (board[3] == board[5] == board[7] == letter) or \
        (board[1] == board[2] == board[3] == letter)


# This function will check for a free space
def is_free(board, position):
    """ is free docstring """
    return board[position] == ' '


# This function will place the marker on the board
def place_marker(board, mark, position):
    """ place marker docstring """
    board[position] = mark


# who goes first
def who_goes_first():
    """ who goes first docstring """
    if random.randint(0, 1) == 0:
        return playerLetter
    else:
        return computerLetter


# player turn
def player_turn():
    """ player turn docstring """
    while True:
        try:
            position = input('Choose a number between 1 & 9: ')
            if re.match(r'^\d+$', str(position)):
                position = int(position)
            else:
                print('Please choose a number between 1 and 9, have another go')  # noqa: E501
                continue
            if position < 1 or position > 9:
                print('Please choose a number between 1 and 9, have another go')  # noqa: E501
            else:
                if is_free(board, position):
                    place_marker(board, playerLetter, position)
                    break
                else:
                    print('This position is not free, please try again')
        except ValueError:
            print("not a valid input")


# create a copy of the board
def duplicate_board(board):
    """ duplicate board docstring """
    duplicate_board = []
    for i in board:
        duplicate_board.append(i)
    return duplicate_board


# computer turn
def computer_turn():
    """ computer turn docstring """
    for i in range(1, 10):
        copy = duplicate_board(board)
        if is_free(copy, i):
            place_marker(copy, computerLetter, i)
            if check_win(copy, computerLetter):
                place_marker(board, computerLetter, i)
                return
        else:
            continue
# check if player can win
    for i in range(1, 10):
        copy = duplicate_board(board)
        if is_free(copy, i):
            place_marker(copy, playerLetter, i)
            if check_win(copy, playerLetter):
                place_marker(board, computerLetter, i)
                return
        else:
            continue
    # If computer plays first corners, middle, and edges
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]  # noqa: E501
    corners = [1, 3, 7, 9]
    edges = [2, 4, 6, 8]
    for i in corners:
        if i in possibleMoves:
            return place_marker(board, computerLetter, i)
    if is_free(board, 5):
        return place_marker(board, computerLetter, 5)
    for i in edges:
        if i in possibleMoves:
            return place_marker(board, computerLetter, i)


# run the game
def main():
    """ run the game docstring """
    print('Welcome to Noughts & Crosses (Tic Tac Toe!)')
    turn = who_goes_first()
    while True:
        if turn == playerLetter:
            print_board()
            player_turn()
            if check_win(board, playerLetter):
                print_board()
                print('You won!')
                break
            elif is_full():
                print_board()
                print('It is a draw!')
                break
            else:
                turn = computerLetter
        else:
            computer_turn()
            if check_win(board, computerLetter):
                print_board()
                print('You lost!')
                break
            elif is_full():
                print_board()
                print('It is a draw!')
                break
            else:
                turn = playerLetter


# start the game
main()
