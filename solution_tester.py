# program tests various proved and theorized solutions to the Ducks and Geese Josephus Game by comparing with simulator
# (c) 2017 David Ariyibi, Williams College, daa1@williams.edu

from josephus_game_simulator import game_parameters, constant_lives, input_lives, josephus

# skip-first solution for survivor in cases when k = 1 and l = 1 (original Josephus Problem)
# (c) Wikipedia/Josephus_problem
def solution_k1_l1(n, s):
    if (n > 1):
        return (solution_k1_l1(n - 1, s) + s) % n
    else:
        return 0

# solution currently being tested
def solution_l1(n, k, s):
    if (n > 1):
        return (solution_l1(n - k, k, s) + s) % n
    else:
        return 0

def test(n, k, s, l, p):
    if (k == 1) and (sum(l) == n):
        print 'k1_l1: ' + str(solution_k1_l1(n, s + 1) - s + p)
    if (sum(l) == n):
        print 'l1: ' + str(solution_l1(n, k, s + 1) - s + p)
    print 'sim: ' + str(josephus(n, k, s, l, p))

if __name__ == '__main__':
    (numb, kill, skip, life, stpt) = game_parameters()
    test(numb, kill, skip, life, stpt)
