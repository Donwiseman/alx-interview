#!/usr/bin/python3
"""
This is a program that solves the N queens puzzle
Usage: nqueens N
       where N is the N queen in an N x N chessboard
"""

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except Exception:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

output_list = []


def check_diag_attck(index_pos, other_queen, row_incr, col_incr, N):
    diagonal_pos = list(index_pos)
    while True:
        diagonal_pos[0] = diagonal_pos[0] + row_incr
        diagonal_pos[1] = diagonal_pos[1] + col_incr
        if diagonal_pos[0] < 0 or diagonal_pos[1] < 0:
            return False
        if diagonal_pos[0] >= N or diagonal_pos[1] >= N:
            return False
        for queen in other_queen:
            if diagonal_pos[0] == queen[0] and diagonal_pos[1] == queen[1]:
                return True


def check_rejection(root, N):
    """Check if the position of the queens are attacking"""
    if len(root) < 2:
        return False
    # the recently appended queen is retrieved as only it can clash
    new_position = root[(len(root) - 1)]
    # check for horizontal attack
    for queen in root[:-1]:
        if new_position[0] == queen[0] or new_position[1] == queen[1]:
            return True
    # check for daigonal attack, starting with top_right attack
    if check_diag_attck(new_position, root[:-1], 1, 1, N):
        return True
    # top-left attack
    if check_diag_attck(new_position, root[:-1], 1, -1, N):
        return True
    # bottom-left attack
    if check_diag_attck(new_position, root[:-1], -1, -1, N):
        return True
    # bottom right attack
    if check_diag_attck(new_position, root[:-1], -1, 1, N):
        return True
    return False


def check_accepted(root, N):
    """Checks if the partial solution meets criteria for solution"""
    # Since rejection function already guarantees non attacking queens
    if len(root) == N:
        return True
    return False


def backtrack(root: list, N: int) -> None:
    """
    Performs the backtract algorithm used to solve the N queen puzzle
    Args:
        root: is the current partial solution in view.
        N: the size of the board and desired queen number.
    """
    if check_rejection(root, N):
        return
    if check_accepted(root, N):
        output_list.append(root)
    if len(root) == N:
        return
    # find next column to expand
    expand_column = len(root)
    for row in range(N):
        new_position = [row, expand_column]
        new_root = list(root)
        new_root.append(new_position)
        backtrack(new_root, N)


backtrack([], N)
for solution in output_list:
    print(solution)
