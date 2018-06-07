# program tests various solutions to parts of the Ducks and Geese Josephus Game
# (c) 2017 David Ariyibi, Williams College, daa1@williams.edu

from sys import argv
import josephus as j
import math as m

def gcd(a,b):
    while b > 0: a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def test(n, k, s, l, p, sf, g):
    print "Game: n=" + str(n) + ", k=" + str(k) + ", s=" + str(s) + ", l=" + str(l) + ", p=" + str(p) + ", sf=" + str(sf)

    # Thm 5.1
    if gcd(n, k + s) == 1 and l > k:
        print "- Thm 5.1"
        l = l - k
        while l > k: l = l - k
        return test(n, k, s, l, p, sf, g)

    # Thm 5.3
    if n % (k + s) == 0:
        print "- Thm 5.3"
        subprob = test(n * s / (k + s), k, s, l, p, sf, g)
        if sf: return (k + s) * (subprob / s) + (subprob % s)
        return (k + s) * (subprob / s) + (subprob % s) - s

    # Thm 5.2
    if s % n == 0 and n % k == 0:
        print "- Thm 5.2"
        l = 1

    # Section 3
    if l == 1:
        print "- l = 1"
        return test_1(n, k, s, l, p, sf, g)

    return unknown()

def test_1(n, k, s, l, p, sf, g):

    # Thm 3.3
    if k % s == 0:
        a = n % k
        if a == 0: a = k

        ks = k + s
        kss = ks / s
        b = 1
        while n >= a * (kss ** b): b = b + 1
        b = b - 1

        m = (n - a * (kss ** b)) / (k + 0.0)
        int_m, akssb = int(m), a * (kss ** b)
        if 0.0 == m - int_m and (akssb % ks == 0 or ks > akssb):
            print "- Thm 3.3"
            if sf: return (ks * int_m + s - 1 + p) % n
            else: return (ks * int_m - 1 + p) % n

    # Thm 3.4, Cor 3.1, Cor 3.2
    if True:
        a = n % k
        if a == 0: a = k

        ks = k + s
        b = 1
        while n >= a * (ks ** b): b = b + 1
        b = b - 1

        m = (n - a * (ks ** b)) / (k + 0.0)
        int_m = int(m)
        km = int_m * (k + 1)
        if 0.0 == m - int_m and km <= n and n <= (int_m + 1) * k:
            ksm = ks * int_m
            if sf: T = (ksm + s - 1 + p) % n
            else: T = (ksm - 1 + p) % n
            if ksm < n:
                print "- Thm 3.4"
                return T

            i = m.ceil((ksm - n) / (s + 0.0)) * k
            if s == 2:
                print "- Cor 3.1"
                T = (T + i) % n
            if s == 3:
                print "- Cor 3.2"
                if int_m < 3: T = (T + i) % n
                else: T = (T + i + k) % n
            return T

    # Thm 3.1
    if n == k + s and k >= s:
        print "- Thm 3.1"
        if sf: return (p - 1 + s) % n
        return (p - 1) % n

    # Prop 3.1, Thm 3.2
    if n < k + s:
        if k >= n:
            print "- Prop 3.1"
            if sf: return (p - 1 + s) % n
            return (p - 1) % n
        if k >= n / 2:
            print "- Thm 3.2"
            a = s % (n - k)
            if a == 0: a = n - k
            if sf: return (k + a + p - 1 + s) % n
            return (k + a + p - 1) % n

    # Thm 3.2
    if k > s and k > n/2:
        print "- Thm 3.2"
        a = s % (n - k)
        if a == 0: a = n - k
        if sf: return (k + a + p - 1 + s) % n
        return (k + a + p - 1) % n

    return unknown()

def unknown():
    print "- unknown -> run simulator"
    return -1

def parse_arg(arg):
    if (len(arg) != 8):
        print len(arg)
        return j.error(0)

    g = False
    if (argv[6] == 's'):
        sf = True
        if (argv[7] == "g"): g = True
    if (argv[6] == 'k'):
        sf = False
        if (argv[7] == "g"): g = True

    return test(int(arg[1]), int(arg[2]), int(arg[3]), int(arg[4]), int(arg[5]), sf, g)

if __name__ == '__main__':
    test = parse_arg(argv)
    if test > -1: print "Test: " + str(test)
    res = j.parse_arg(argv)
    print "Actual: " + str(res[-1])
