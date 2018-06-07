# simulates the Ducks and Geese Josephus Game and its subset of Josephus games
# (c) 2017 David Ariyibi, Williams College, daa1@williams.edu

from sys import argv

# input:  num of people, kill length, skip length, lives per person, start-point,
#         skip-first/kill-first, include graphic
# output: list of players in order of death and optional graphic of how players are killed
def josephus(n, k, s, l, p = 0, sf = False, show = False):
    # initializes graphic
    show_list = []
    for i in range(n):
        if i < 10: show_list.append(' ' + str(i) + ':')
        else: show_list.append(str(i) + ':')

    # indexes graphic to start at person p
    b = 0
    while b < p:
        show_list[b] = show_list[b] + " _"
        b = b + 1

    # initial skips (if any)
    if sf:
        c = p # stops infinite loop if p + s >= n
        while c < b + s:
            show_list[p] = show_list[p] + " O"
            c, p = c + 1, (p + 1) % n

    dead_list = []
    total_lives = sum(l)
    while total_lives > 0:

        # killing
        for i in range(k):
            if total_lives > 0: # stops an infinite loop of all dead players
                is_dead = False # skips players who are already dead
                while not is_dead:
                    p = p % n # keeps pointer from going out of bounds
                    lives = l[p]
                    if lives > 0:
                        lives, total_lives = lives - 1, total_lives - 1 # player loses a life
                        l[p] = lives # updates player's life amount
                        is_dead = True
                        if lives == 0: dead_list.append(p) # if player is dead, adds them to dead_list
                        show_list[p] = show_list[p] + " X"
                    else: show_list[p] = show_list[p] + " _"
                    p = p + 1 # moves on to next players

        # skipping
        for j in range(s):
            if total_lives > 0:
                success = False
                while not success:
                    p = p % n
                    if l[p] > 0:
                        show_list[p] = show_list[p] + " O"
                        success = True
                    else: show_list[p] = show_list[p] + " _"
                    p = p + 1

    # prints graphic
    if show:
        for m in show_list:
            print m

    return dead_list

# creates list where all players in game have the same number of initial lives
def constant_lives(i, n):
    life_array = [i] * n
    return life_array

# creates list where user decides the initial life amount for each player
def input_lives(n):
    life_array = [0] * n
    for i in xrange(n):
        life_array[i] = int(raw_input("Number of lives for player " + str(i) + ": "))
    return life_array

# parses arguments and runs game accordingly
# arg = [n, k, s, l, p, -s/-k, -g/-n]
def parse_arg(arg):
    if (len(arg) != 8): return error(0)

    n = int(arg[1])
    if (argv[6] == '-s'):
        if (argv[7] == "-g"):
            return josephus(n, int(arg[2]), int(arg[3]), constant_lives(int(arg[4]), n), int(arg[5]), True, True)
        elif (argv[7] == "-n"):
            return josephus(n, int(arg[2]), int(arg[3]), constant_lives(int(arg[4]), n), int(arg[5]), True, False)
    elif (argv[6] == '-k'):
        if (argv[7] == "-g"):
            return josephus(n, int(arg[2]), int(arg[3]), constant_lives(int(arg[4]), n), int(arg[5]), False, True)
        elif (argv[7] == "-n"):
            return josephus(n, int(arg[2]), int(arg[3]), constant_lives(int(arg[4]), n), int(arg[5]), False, False)
    return error(1)

# error cases
def error(i = -1):
    if i == 0: return "Invalid entry: length"
    elif i == 1: return "Invalid entry: syntax"
    else: return "Invalid entry: unknown"

if __name__ == '__main__':
    print parse_arg(argv)
