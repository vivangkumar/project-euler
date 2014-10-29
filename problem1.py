__author__ = 'Vivan'

'''
Problem 1: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.
Find the sum of all multiples of 3 or 4 below 1000.
'''


def multiples():
    sum = 0
    for num in range (1,1000):
        # We check for mod 3 or mod 5 to see if the remainder is 0.
        # If remainder is 0, it means the numbers are divisible by 3 and 5 and are consequently multiples of 3 and 5.
        if(num % 3 == 0 or num % 5 == 0):
            sum += num
    return sum

print multiples()



