#!/usr/bin/python3
"""
Solves the make challenge problem using backtracking algorithmn.
"""


def makeChange(coins: list, total):
    """Finds the least coin change combination"""
    coins_number = 0
    final_coins_number = 0
    if total <= 0:
        return -1
    coins.sort(reverse=True)
    for index, value in enumerate(coins):
        if value > total:
            continue
        coins_number = total // value
        total_remainder = total % value
        if total_remainder == 0:
            if not final_coins_number:
                final_coins_number = coins_number
                continue
            elif coins_number < final_coins_number:
                final_coins_number = coins_number
                continue
            continue
        more_coins = makeChange(coins, total_remainder)
        if more_coins == -1:
            continue
        coins_number += more_coins
        if not final_coins_number:
            final_coins_number = coins_number
            continue
        elif coins_number < final_coins_number:
            final_coins_number = coins_number
            continue
    if not final_coins_number:
        return -1
    return final_coins_number
