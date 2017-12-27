# program creates table of the Ducks and Geese Josephus Game survivors under various parameters
# program only works for constant-life parameters
# (c) 2017 David Ariyibi, Williams College, daa1@williams.edu

from josephus_game_simulator import game_parameters, constant_lives, josephus
import csv

# interface for assigning parameters for table
def table_parameters():
    while True:
        dimm = int(raw_input("Number of iterations: "))
        if (dimm > 0):
            break
    while True: # in case of wrong input
        incr = raw_input("Are we incrementing skipping or killing? ('s' or 'k'): ")
        if (incr == 's') or (incr == 'k'):
            break
    return (dimm, incr)

# creates a table of survivors with each row being how many people and col being how many kills/skips
def survivor_table(n = 1, k = 1, s = 1, l = 1, p = 0, dimm = 100, incr = 'k'):
    s_table = [[0]*dimm for _ in xrange(dimm)
    i_index = xrange(len(s_table))
    j_index = xrange(len(s_table[0]))
    if (incr == 'k'): # kill increases
        for i in i_index:
            for j in j_index:
                new_life = constant_lives(l, n + i)
                dead = josephus(n + i, k + j, s, new_life, p)
                s_table[i][j] = dead[-1]
    if (incr == 's'): # skip increases
        for i in i_index:
            for j in j_index:
                new_life = constant_lives(l, n + i)
                dead = josephus(n + i, k, s + j, new_life, p)
                s_table[i][j] = dead[-1]
    return s_table

# similar to survivor_table but also increases player lives with each column
def survivor_table_l(n = 1, k = 1, s = 1, l = 1, p = 0, dimm = 100, incr = 'k'):
    s_table = [[0]*dimm for _ in xrange(dimm)]
    i_index = xrange(len(s_table))
    j_index = xrange(len(s_table[0]))
    if (incr == 'k'): # kill increases
        for i in i_index:
            for j in j_index:
                new_life = constant_lives(l + j, n + i)
                dead = josephus(n + i, k + i, s, new_life, p)
                s_table[i][j] = dead[-1]
    if (incr == 's'): # skip increases
        for i in i_index:
            for j in j_index:
                new_life = constant_lives(l + j, n + i)
                dead = josephus(n + i, k, s + i, new_life, p)
                s_table[i][j] = dead[-1]
    return s_table

def create_csv(table, fn):
    with open(fn + '.csv', 'wb') as myfile:
        wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
        for i in s_table:
            wr.writerow(i)

if __name__ == '__main__':
    (numb, kill, skip, life, stpt) = game_parameters()
    (dimm, incr) = table_parameters()
    filename = raw_input("Filename: ")
    create_csv(survivor_table(numb, kill, skip, life[0], stpt, dimm, incr), filename)
