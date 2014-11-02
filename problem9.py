__author__ = 'Vivan'

'''
a = m^2 - n^2
b = 2nm
c = m^2 + n^2
where m < n
'''

def pythagorean_triplet():
    for m in range(1, 300):
        for n in range(2, 300):
            a = m*m - n*n
            b = 2 * m * n
            c = m*m + n*n

            if(a + b + c) == 1000:
                print a * b * c

pythagorean_triplet()