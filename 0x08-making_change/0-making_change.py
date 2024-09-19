#!/usr/bin/python3


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to
    meet a given amount total.
    :param coins: List of coin denominations
    :param total: The target amount
    :return: Fewest number of coins needed to
    meet the total, or -1 if not possible
    """
    if total <= 0:
        return 0
    # Initialize DP array with
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    # Process each coin and update the dp table
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    # Return -1 if no combination of coins  total
    return dp[total] if dp[total] != float('inf') else -1
