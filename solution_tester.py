# program tests various proved solutions from the Extended Feline Josephus Game paper
# Theorem and Proposition numbers correspond to paper
# (c) 2017 David Ariyibi, Williams College, daa1@williams.edu

from sys import argv
import josephus as j
import math as m

# tests solutions where l >= 1
def test(n, k, s, l, p, sf, g):
    print "Game: n=" + str(n) + ", k=" + str(k) + ", s=" + str(s) + ", l=" + str(l) + ", p=" + str(p) + ", sf=" + str(sf)

    # Prop 4
    if n * l <= k:
        print "- Prop 4"
        if sf: return (s - 1 + p) % n
        return (p - 1) % n

    # Prop 5
    if k % n == 0:
        print "- Prop 5"
        if sf: return (s * int(m.ceil(n * l / (k + 0.0))) - 1 + p) % n
        return (s * int(m.ceil(n * l / (k + 0.0))) - s - 1 + p) % n

    # Prop 6
    if s % n == 0 and k >= n:
        print "- Prop 6"
        total = n * l
        a = total / k * k
        if total == a:
            print "--- total == a"
            return (p - 1) % n
        if total - a >= n:
            print "--- total - a >= n"
            return (p - 1) % n
        return ((s % (total - a)) + a - 1 + p) % n
    
    # Thm 5
    if gcd(n, k + s) == 1 and l > k:
        print "- Thm 5"
        l = l - k
        while l > k: l = l - k
        return test(n, k, s, l, p, sf, g)

    # Thm 6
    if l > 1 and s % n == 0 and n % k == 0:
        print "- Thm 6"
        return test(n, k, s, 1, p, sf, g)

    # Thm 7
    kn = int(m.ceil(k / (n + 0.0)))
    if (k + s) % n == 0 and l % kn == 0:
        print "- Thm 7"
        a = k % n
        if sf: return test(s % n, k, s, l - ((k - a) * l / (n * kn)), p, sf, g)
        return (test(s % n, k, s, l - ((k - a) * l / (n * kn)), p, sf, g) - s) % n

    # Thm 8
    if n % (k + s) == 0:
        print "- Thm 8"
        subprob = test(n * s / (k + s), k, s, l, p, sf, g)
        if sf: return (k + s) * (subprob / s) + (subprob % s)
        return ((k + s) * (subprob / s) + (subprob % s) - s) % n

    # Thm 9
    a = gcd(gcd(n, k), s)
    if a > 1:
        print "- Thm 9"
        subprob = test(n / a, k / a, s / a, l, 0, sf, g)
        return (a * subprob + a - 1 + p) % n

    if l == 1:
        print "- l = 1"
        return test_1(n, k, s, l, p, sf, g)

    return -1

# tests solutions where l == 1
def test_1(n, k, s, l, p, sf, g):

    # Prop 1
    if n <= k:
        print "- Prop 1"
        if sf: return (s - 1 + p) % n
        return (p - 1) % n

    # Prop 2
    if n == k + s and k >= s:
        print "- Prop 2"
        if sf: return (p - 1 + s) % n
        return (p - 1) % n

    # Prop 3
    if k >= n / 2:
        print "- Prop 3"
        a = s % (n - k)
        if a == 0: a = n - k
        if sf: return (k + a + p - 1 + s) % n
        return (k + a + p - 1) % n

    # Thm 3
    if k % s == 0:
        a = n % k
        if a == 0: a = k
        print "a: " + str(a)

        ks = k + s
        kss = ks / s
        b = 1
        while n >= a * (kss ** b): b = b + 1
        b = b - 1
        print "b: " + str(b)

        akssb = a * (kss ** b)
        m = (n - akssb) / (k + 0.0)
        int_m = int(m)
        print "m: " + str(int_m)

        if ks >= akssb or akssb % ks == 0 and 0.0 == m - int_m:
            print "- Thm 3"
            if sf: return (ks * int_m + s - 1 + p) % n
            return (ks * int_m - 1 + p) % n

    # Thm 4
    if True:
        a = n % k
        if a == 0: a = k
        print "a: " + str(a)

        ks = k + s
        b = 1
        while n >= a * (ks ** b): b = b + 1
        b = b - 1
        print "b: " + str(b)

        m = (n - a * (ks ** b)) / (k + 0.0)
        int_m = int(m)
        print "m: " + str(int_m)
     
        ksm = (k + s) * int_m
        if 0.0 == m - int_m and ksm < n and n <= (int_m + 1) * k:
            print "- Thm 4"
            if sf: return (ksm + s - 1 + p) % n
            return (ksm - 1 + p) % n

    return -1

# greatest common denominator
def gcd(a,b):
    while b > 0: a, b = b, a % b
    return a

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
    print "Test: " + str(parse_arg(argv))
    print "Actual: " + str(j.parse_arg(argv)[-1])
