__author__ = 'vivan'

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


def largest_prime_factor(n):
    factors = []
    div = 2

    while n > 1:
        while n % div == 0:
            factors.append(div)
            n /= div
        div += 1
        if div*div > n:
            factors.append(n)
            break
    return max(factors)

print largest_prime_factor(600851475143)

