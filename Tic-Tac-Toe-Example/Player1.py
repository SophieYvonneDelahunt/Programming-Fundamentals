# Player1.py
#
# author: Stephen Adams
# date  : 2024-10-19
#
# Temporary modification by Sophie Delahunt! Just this comment.
#
# This file contains the code for Player 1 in a Tic-Tac-Toe game. It is intentionally not simplified or generalized to
# attempt to avoid merge conflicts between the partners.
import random

def getValue( board, position ):
    """
    Returns the value at the given position on the board, from the simple 1-9 index.
    """
    return board[ (position - 1) // 3 ][ (position - 1) % 3 ]

def horizontal_verifier (A,board):
    row_checker = False
    space_checker = 0

    for i in range(A,A + 3):
        if getValue( board, i ) == "O":
            row_checker = True
        if getValue( board, i ) == " ":
            space_checker = i
    return row_checker, space_checker

def vertical_verifier (A,board):
    column_checker = False
    space_checker = 0

    for i in range(A,A + 6,3):
        if getValue( board, i ) == "O":
            column_checker = True
        if getValue( board, i ) == " ":
            space_checker = i
    return column_checker, space_checker

def getMove(board):
    """
    Determines the next move for Player 1. Player 1 will always be 'X'.
    
    Since studnets will not have yet learned lists, we will use indicies 1-9 to represent the Tic-Tac-Toe board as follows:

        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9

    To avoid requring list notation in this function, we will use the getValue function to get the value at a given position.

    Parameters:
    board (list of list of str): The current state of the Tic-Tac-Toe board.

    Returns:
    integer: The index of the next move between 1 and 9.
    """
    for i in range (1,8,3):
        row_checker, space_checker = horizontal_verifier (i, board)

        if row_checker == False:
            return space_checker
    
    for i in range (1,4,1):
        column_checker, space_checker = vertical_verifier (i, board)

        if column_checker == False:
            return space_checker
    
    # The following checks for diagonal lines.
    
    if ( getValue( board, 1 ) == " " and getValue( board, 5 ) == "X" and getValue( board, 9 ) == "X" ):
        return 1
    if ( getValue( board, 3 ) == " " and getValue( board, 5 ) == "X" and getValue( board, 7 ) == "X" ):
        return 3
    if ( getValue( board, 9 ) == " " and getValue( board, 5 ) == "X" and getValue( board, 1 ) == "X" ):
        return 9
    if ( getValue( board, 7 ) == " " and getValue( board, 5 ) == "X" and getValue( board, 3 ) == "X" ):
        return 7
    else:
        return random.randint(1, 9)