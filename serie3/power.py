def mod_power(z, b, k, n):
    return z**b**k % n

def mod_infinite_power(tab, n):
    calc = 1
    tab.reverse()
    for val in tab:
        calc= val**calc
    return calc%n


if __name__ == '__main__':
    print(mod_power(3,4,2,11))

    print(mod_infinite_power([2,2,2,2], 65537))
