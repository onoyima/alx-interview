#!/usr/bin/python3
"""
Module 0-making_change
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total
    Arguments:
    coins -- list of the values of the coins in possession
    total -- total amount to achieve with the fewest number of coins
    Return:
    The fewest number of coins needed to meet the total
    If total is 0 or less, return 0
    If total cannot be met, return -1
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins
    # required for each amount up to 'total'
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Zero coins are needed to make a total of 0

    # Dynamic programming to fill the dp list
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
