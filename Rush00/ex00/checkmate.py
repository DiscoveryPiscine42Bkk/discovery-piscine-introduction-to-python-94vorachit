#!/usr/bin/env python3

def checkmate():
    character = [".","P","B","R","Q","K"]

    
#-------------------------------------------------------------------------------
# check king valid moves
def check_king(position):
    moves_list = []
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0),
               (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list
#-------------------------------------------------------------------------------
# check bishop moves
def check_bishop(position):
    moves_list = []
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append(
                    (position[0] + (chain * x), position[1] + (chain * y)))
#                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
#                    path = False
                chain += 1
            else:
                path = False
    return moves_list
#-------------------------------------------------------------------------------
# check rook moves
def check_rook(position):
    moves_list = []
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append(
                    (position[0] + (chain * x), position[1] + (chain * y)))
#                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
#                    path = False
                chain += 1
            else:
                path = False
    return moves_list
#-------------------------------------------------------------------------------
# check queen valid moves
def check_queen(position):
    moves_list = check_bishop(position)
    second_list = check_rook(position)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list
#-------------------------------------------------------------------------------
# check valid pawn moves
def check_pawn(position, color):
    moves_list = []
    if (position[0], position[1] + 1) not in white_locations and \
        (position[0], position[1] + 1) not in black_locations and position[1] < 7:
        moves_list.append((position[0], position[1] + 1))
    if (position[0], position[1] + 2) not in white_locations and \
        (position[0], position[1] + 2) not in black_locations and position[1] == 1:
        moves_list.append((position[0], position[1] + 2))
    if (position[0] + 1, position[1] + 1) in black_locations:
        moves_list.append((position[0] + 1, position[1] + 1))
    if (position[0] - 1, position[1] + 1) in black_locations:
        moves_list.append((position[0] - 1, position[1] + 1))

    return moves_list