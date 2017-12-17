"""
@author Michael Zeng, Teemu Virtanen
"""

import time

def primes(primes_list, n):
    i = primes_list[-1] + 1
    while len(primes_list) < n:
        prime = True
        for x in primes_list:
            if i % x == 0:
                prime = False
                break
        if not prime:
            i += 1
        else:
            primes_list.append(i)
    return primes_list

list_of_primes = [2,3,5,7,11,13]
nth = 0
while True:
    try:
        nth = int(input('nth prime: '))
        break
    except ValueError:
        print('n must be an integer.')
while nth <= 0:
    print('Enter a value greater than 0.')
    nth = int(input('nth prime: '))
t = time.time()
nth_prime = -1
if nth <= 6:
    nth_prime = list_of_primes[nth-1]
else:
    list_of_primes = primes(list_of_primes, nth)
    nth_prime = list_of_primes[-1]
print(nth_prime)
elapsed = time.time() - t
print('Executed in {0} seconds.'.format(elapsed))
