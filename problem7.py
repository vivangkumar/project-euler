__author__ = 'Vivan'

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
************************
May be quite inefficient
'''


def prime_position():
    count = 0
    num = 0
    while True:
        num += 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                count += 1
                if count == 10001:
                    print num
                    break


prime_position()

