from math import gcd
from timer import timed

def digit_diff(a, b):
    # returns the number of digits that different between two numbers
    a_lst, b_lst = list(str(a)), list(str(b))
    count = 0
    for i in a_lst:
        if i in b_lst and a % 10 and b % 10:
            count += 1
            b_lst.remove(i)
    return count

def cancelling_fallacy(numerator, denominator):
    assert numerator < 100 and denominator < 100

    # remove the digits from the numerator and denominator that are the same
    numer_lst, denom_lst = list(str(numerator)), list(str(denominator))
    for digit in numer_lst:
        if digit in denom_lst:
            numer_lst.remove(digit)
            denom_lst.remove(digit)

    # check whether the new fraction is the same as the original
    if numerator / denominator == int(numer_lst[0]) / int(denom_lst[0]):
        print('{0} / {1} = {2} / {3}'.format(numerator, denominator, int(numer_lst[0]), int(denom_lst[0])))
        return [int(numer_lst[0]), int(denom_lst[0])] #True value
    else:
        return False

@timed
def digit_cancelling_fractions():
    fractions = []
    for numer in range(10, 100):
        for denom in range(numer, 100):
            if digit_diff(numer, denom) == 1:
                cancel_works = cancelling_fallacy(numer, denom)
                if cancel_works:
                    fractions.append(cancel_works)
    return fractions

def product_fracs(frac_list):
    # returns denominator of the simplified product of the fractions in a list
    numer_product, denom_product = 1, 1
    for fraction in frac_list:
        numer_product *= fraction[0]
        denom_product *= fraction[1]
    return denom_product // gcd(numer_product, denom_product)

print(product_fracs(digit_cancelling_fractions()))
