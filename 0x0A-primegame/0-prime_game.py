#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """Determines the winner after x rounds of the prime game"""
    if x <= 0 or not nums:
        return None


"""# Maximum number for the sieve"""
    max_n = max(nums)
    
    """ Use Sieve of Eratosthenes to precompute
    prime numbers up to max_n"""
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False
    """0 and 1 are not prime numbers"""

    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, max_n + 1, i):
                primes[j] = False

    """ # To track the number of wins by each player"""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(primes[0:n+1])
        """Count primes up to n"""
    """# Maria wins if the count of primes is odd,
    Ben wins if it's even"""
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


"""# Helper function to check if a number is prime
(no longer needed with sieve)"""
def rm_multiples(ls, x):
    """Removes multiples of a prime number"""
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
