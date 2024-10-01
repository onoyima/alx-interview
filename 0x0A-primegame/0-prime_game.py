#!/usr/bin/python3


def sieve_of_eratosthenes(n):
    """Generate a list of primes up to n using the Sieve of Eratosthenes"""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def isWinner(x, nums):
    """
    Determine the winner of each game.
    
    :param x: Number of rounds.
    :param nums: List of 'n' values for each round.
    :return: Name of the player that won the most rounds, or None if it's a tie.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes_up_to_max_n = sieve_of_eratosthenes(max_n)

    # Memoization for each n up to max_n
    prime_count_up_to = [0] * (max_n + 1)

    # Count the number of primes up to each number n
    for i in range(2, max_n + 1):
        prime_count_up_to[i] = prime_count_up_to[i - 1] + (1 if i in primes_up_to_max_n else 0)

   maria = 0
    ben = 0

    for n in nums:
        if prime_count_up_to[n] % 2 == 1:
            # If the number of primes is odd, Maria wins (she goes first)
           maria += 1
        else:
            # If the number of primes is even, Ben wins
            ben += 1

    ifmaria > ben:
        return "Maria"
    elif ben >maria:
        return "Ben"
    else:
        return None


# Sample usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
