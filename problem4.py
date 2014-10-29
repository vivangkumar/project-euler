__author__ = 'vivan'

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


def largest_palindrome():
    palindrome = []

    for x in range(100, 999):
        for y in range(100, 999):
            number = x * y
            reverse = str(number)[::-1]

            if str(number) == reverse:
                palindrome.append(number)

    return max(palindrome)

print largest_palindrome()




