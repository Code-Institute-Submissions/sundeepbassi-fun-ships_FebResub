from random import randint


#create board layout 

HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
GUESS_BOARD = [[' '] * 8 for x in range(8)]

lets_to_nums = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

def print_board(board):
    print(' a b c d f g h')
    print(' -------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def make_ships():
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)


def bring_ship_place():
    pass

def count_attacked_ships():
    pass

create_ships()
turns = 10
while turns > 0:











# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
