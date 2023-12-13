#!/usr/bin/python3
""" Solves the minimum operation challenge. """


def isDivisible(numerator: int, denominator: int) -> bool:
    """Check if a given numerator is wholly divisible by denominator."""
    if numerator % denominator == 0:
        return True
    else:
        return False


def minOperations(n: int) -> int:
    """ Calculates the minimum operation to print n Hs."""
    op_count = 0
    h_num = 1
    clipboard = 0
    while True:
        remainder = n - h_num
        if remainder <= 0:
            return op_count
        if isDivisible(remainder, h_num):
            # copy first
            op_count += 1
            clipboard = h_num
            # then Paste
            op_count += 1
            h_num += clipboard
        elif isDivisible(remainder, clipboard):
            # Paste
            op_count += 1
            h_num += clipboard
        else:
            return 0
