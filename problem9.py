__author__ = 'Vivan'

def pythagorean_triplet():
    a, b, result = 0, 0, []
    for c in range(1, 1000):
        if c - 2 > 0:
            a = c - 2
            b = c - 1
            print a, b, c

pythagorean_triplet()