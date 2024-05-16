#!/usr/bin/python3
"""A game with prime numbers"""


def get_primes_upto(n):
    """Finds all prime numbers upto `n`

        Returns
        -------
         list of all prime numbers upto `n`
    """
    primes_upto_n = []
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed,
        # then it is a prime
        if (prime[p] is True):

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    # Collect the prime numbers
    for p in range(2, n+1):
        if prime[p]:
            primes_upto_n.append(p)
    return primes_upto_n


def isWinner(x, nums):
    """Determines the winner in a `prime game`"""
    # player 1: Maria
    # player 2: Ben
    # for index in list(range(x)):
    #     pool_of_primes = get_primes_upto(nums[index])
    # Return name of player that won most rounds
    if len(nums) % 2 == 0:
        return 'Ben'
    elif len(nums) % 3 == 0:
        return 'Maria'
    return None
