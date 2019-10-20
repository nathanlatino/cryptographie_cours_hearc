import math
from builtins import range
from datetime import datetime


def is_prime(n):
    if (n >= 2):
        for i in range(2, n):
            if not (n % i):
                return False
    else:
        return False
    return True


def prime_factors(n):
    factors = []
    while n % 2 == 0:
        n = n / 2
        factors.append(2)

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n = n / i
            factors.append(i)

    if n > 2:
        factors.append(int(n))

    return factors


def find_primes(n):
    primes = []
    for i in range(2, n):
        if is_prime(i): primes.append(i)
    return primes


def prime_counting(n):
    return len(find_primes(n))


def gcd_loop(x, y):
    for i in range(1, (x if x > y else y) + 1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd


# better
def gcd_euclide(x, y):
    while y:
        x, y = y, x % y
    return x


def euler_totient(n):
    res = 1
    for i in range(2, n):
        if gcd_euclide(i, n) == 1: res += 1
    return res


def euler_theorem(a, n):
    return a ** euler_totient(n)


def extended_euclid(a, b):
    s = 0
    t = 1
    r = b
    old_s = 1
    old_t = 0
    old_r = a
    while r != 0:
        quotient = int(old_r / r)
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    print(f"Bézout coefficients: {old_s}, {old_t}")
    print(f"greatest common divisor: {old_r}")
    print(f"quotients by the gcd: {t}, {s}")


def modular_pow(a, exp, n):
    c = 1
    a = a % n
    while exp > 0:
        if exp % 2 == 1:
            c = (c * a) % n
        exp = exp >> 1
        a = (a * a) % n
    return c


def straightforward_pow(a, exp, n):
    c = a ** exp
    return c % n


def mod_pow(a, exp, n):
    c = 1
    for i in range(0,exp):
        c = (c * a) % n
    return c


if __name__ == '__main__':
    n = 2038074743
    a = 987654321
    exp = 1234551
    start = datetime.now(tz=None)

    # print(gcd_loop(7, 14))
    # print(prime_factors(2))
    # print(euler_totient())
    # print(euler_theorem(a, n))
    start = datetime.now(tz=None)
    print(straightforward_pow(a, exp, n))
    print(f"straightforward time : {datetime.now(tz=None) - start}\n")

    start = datetime.now(tz=None)
    print(mod_pow(a, exp, n))
    print(f"advanced algo time : {datetime.now(tz=None) - start}\n")

    start = datetime.now(tz=None)
    print(modular_pow(a,exp,n))
    print(f"optimised algo time : {datetime.now(tz=None) - start}\n")


