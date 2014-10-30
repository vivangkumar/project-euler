__author__ = 'Vivan'


#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sum_square_difference():
    square_total, square_sum, total, diff, num, x = 0, 0, 0, 0, 100, 1

    while x <= num:
        square_total += x*x
        total += x
        square_sum = total*total
        x += 1
    diff = square_sum - square_total
    return diff

print sum_square_difference()

