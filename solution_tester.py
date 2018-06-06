# program tests various proved and theorized solutions to the Ducks and Geese Josephus Game by comparing with simulator
# (c) 2017 David Ariyibi, Williams College, daa1@williams.edu

from sys import argv
import josephus as j
import math

def gcd(a,b):
    while b > 0: a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def unknown():
    print "-- unknown -> run simulator"
    return -1

# skip-first solution for survivor in cases when k = 1 and l = 1 (original Josephus Problem)
# (c) Wikipedia/Josephus_problem
def k1_l1(n, s):
    if n > 1:
        if n >= s:
            n_prime = n - (n / s)
            return s * ((k1_l1(n_prime, s) - n % s) % n_prime) / (s - 1)
        return (k1_l1(n - 1, s) + s) % n
    return 0

def test(n, k, s, l, p, sf, g):
    print "Game: n=" + str(n) + ", k=" + str(k) + ", s=" + str(s) + ", l=" + str(l) + ", p=" + str(p) + ", sf=" + str(sf)

    # # Section 4: Proposition 4.1
    # if gcd(n, k + s) == 1 and l > k:
    #     print "- Reduce l"
    #     l = l - k
    #     while l > k: l = l - k
    #     return test(n, k, s, l, p, sf, g)
    #
    # # Section 4: Theorem 4.2
    # if n % (k + s) == 0:
    #     print "- Reduce n"
    #     subprob = test(n * s / (k + s), k, s, l, p, sf, g)
    #     if sf: return (k + s) * (subprob / s) + (subprob % s)
    #     return (k + s) * (subprob / s) + (subprob % s) - s

    # Section 3 Solutions
    if l == 1:
        print "- l = 1"
        return test_l1(n, k, s, l, p, sf, g)

    return unknown()

def test_l1(n, k, s, l, p, sf, g):
    # Used for Theorems 3.3 and 3.4
    # find a where 1 <= a <= k such that a = n mod
    a = n % k
    if a == 0: a = k

    # Section 3: Theorem 3.3
    if k % s == 0:
        # find largest b such that n >= a * (((k + s)/s) ^ b)
        ks = k + s
        kss, b = ks / s, 1
        while n >= a * (kss ** b): b = b + 1
        b = b - 1

        # let m = (n - a * (((k + s)/s) ^ b)) / k
        m = (n - a * (kss ** b)) / (k + 0.0)

        # survivor is T(n, k, s) = (k + s) * m + s - 1
        int_m, akssb = int(m), a * (kss ** b)
        if math.ceil(m) == math.floor(m) and (akssb % ks == 0 or ks > akssb):
            # return (ks * int_m + s - 1 + p) % n
            if sf: print "Test.1: " + str((ks * int_m + s - 1 + p) % n)
            else: print "Test.1: " + str((ks * int_m - 1 + p) % n)
        print "---- incorrect form"
    # return -1

    # Section 3: Theorem 3.4
    if True:
        # find largest b such that n >= a * ((k + s) ^ b)
        ks, b = k + s, 1
        while n >= a * (ks ** b): b = b + 1
        b = b - 1

        # let m = (n - a * ((k + s) ^ b)) / k
        m = (n - a * (ks ** b)) / (k + 0.0)

        # survivor is T(n, k, s) = (k + s) * (m + floor((a * s ^ b) /k)) + s - 1
        m_ = int(m)
        km = m_ * (k + 1)
        if math.ceil(m) == math.floor(m) and km <= n and n <= (m_ + 1) * k: # and n <= k * (k + 1):

            if s > 1:
                i, sm = n - km, (s - 1) * m_
                if i < sm:
                    # j = math.ceil((sm - i) / (s + 0.0))
                    # if sf: return (ks * m_ + (k * j) + s - 1 + p) % n
                    # return (ks * m_ + (k * j) - 1 + p) % n
                    return -1

            if sf: return (ks * m_ + s - 1 + p) % n
            return (ks * m_ - 1 + p) % n
            # return m_

        print "---- incorrect form"
    return -1

    # Wikipedia/Josephus_problem solution
    if k == 1:
        print "-- k = 1"
        if sf: return k1_l1(n, s)
        return k1_l1(n, s) - s

    # Section 3: Theorem 3.2
    if n == k + s:
        print "-- n = k + s"
        if k >= s:
            print "--- k >= s"
            if sf: return (p - 1 + s) % n
            return (p - 1) % n
        print "--- k < s"
        return unknown()

    # Section 3.1: Theorem ?
    if n < k + s:
        print "-- n < k + s"
        if k >= n:
            print "--- k >= n"
            if sf: return (p - 1 + s) % n
            return (p - 1) % n
        if k >= n/2:
            print "--- k >= n/2"
            a = s % (n - k)
            if a == 0: a = n - k
            if sf: return (k + a + p - 1 + s) % n
            return (k + a + p - 1) % n
        print "--- k < n/2"
        return unknown()

    # Section 3.1: Theorem ?
    print "-- n > k + s"
    if k > s and k > n/2:
        print "--- k > s and k >= n/2"
        a = s % (n - k)
        if a == 0: a = n - k
        if sf: return (k + a + p - 1 + s) % n
        return (k + a + p - 1) % n
    print "--- k <= s or k < n/2"
    return unknown()

def parse_arg(arg):
    if (len(arg) != 8):
        print len(arg)
        return j.error(0)

    if (argv[6] == '-s'):
        sf = True
        if (argv[7] == "-g"): g = True
        if (argv[7] == "-n"): g = False
    if (argv[6] == '-k'):
        sf = False
        if (argv[7] == "-g"): g = True
        if (argv[7] == "-n"): g = False

    return test(int(arg[1]), int(arg[2]), int(arg[3]), int(arg[4]), int(arg[5]), sf, g)

if __name__ == '__main__':
    print parse_arg(argv)
    res = j.parse_arg(arg)
    print "Actual: " + str(res[-1])
