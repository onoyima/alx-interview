#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """ Generate a list of primes up to n using the Sieve of Eratosthenes """
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not primes
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

def count_prime_moves(n, primes):
    """ Count how many moves are possible given a set of numbers up to n """
    taken = [False] * (n + 1)
    moves = 0
    
    for num in range(2, n + 1):
        if primes[num] and not taken[num]:  # If it's a prime and not taken
            moves += 1
            # Remove the prime and its multiples
            for multiple in range(num, n + 1, num):
                taken[multiple] = True
    return moves

def isWinner(x, nums):
    """ Determine the winner after x rounds of the game """
    if x == 0 or not nums:
        return None

    max_n = max(nums)  # Get the largest number in nums
    primes = sieve_of_eratosthenes(max_n)
    
    maria_wins = 0
    ben_wins = 0

    # Play x rounds
    for n in nums:
        moves = count_prime_moves(n, primes)
        # If the number of moves is odd, Maria wins; otherwise, Ben wins
        if moves % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
