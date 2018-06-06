# program creates table of the Ducks and Geese Josephus Game survivors under various parameters
# program only works for constant-life parameters
# (c) 2017 David Ariyibi, Williams College, daa1@williams.edu

from josephus import josephus, input_lives, constant_lives
from josephus_game_simulator import game_parameters
import solution_tester as st
import csv

# interface for assigning parameters for table
def table_parameters():
    while True:
        dimm = int(raw_input("Number of iterations: "))
        if (dimm > 0): break
    while True: # in case of wrong input
        incr = raw_input("Are we incrementing skipping or killing? ('s' or 'k'): ")
        if (incr == 's') or (incr == 'k'): break
    return (dimm, incr)

# creates a table of survivors with each row being how many people and col being how many kills/skips
def survivor_table(n = 1, k = 1, s = 1, l = 1, p = 0, dimm = 100, incr = 'k'):
    s_table = [[0]*dimm for _ in xrange(dimm)]
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

# creates a table of survivors with each row being how many people and col being how many kills/skips
def survivor_table_st(n = 1, k = 1, s = 1, l = 1, p = 0, sf = False, dimm = 100, incr = 'k'):
    s_table = [[0]*dimm for _ in xrange(dimm)]
    i_index = xrange(len(s_table))
    j_index = xrange(len(s_table[0]))
    if (incr == 'k'): # kill increases
        for i in i_index:
            for j in j_index:
                new_life = constant_lives(l, n + i)
                dead = josephus(n + i, k + j, s, new_life, p, sf)
                dead_st = st.test(n + i, k + j, s, l, p, sf, False)
                if dead_st == -1: s_table[i][j] = 0.5
                elif dead[-1] == dead_st: s_table[i][j] = 1
                else: s_table[i][j] = 0
    if (incr == 's'): # skip increases
        for i in i_index:
            for j in j_index:
                new_life = constant_lives(l, n + i)
                dead = josephus(n + i, k, s + j, new_life, p, sf)
                dead_st = st.test(n + i, k, s + j, l, p, sf, False)
                if dead_st == -1: s_table[i][j] = 0.5
                elif dead[-1] == dead_st: s_table[i][j] = 1
                else: s_table[i][j] = 0
    return s_table

def survivor_table_stt(n = 1, k = 1, s = 1, l = 1, p = 0, sf = False, dimm = 100, incr = 'k'):
    s_table = [[0]*dimm for _ in xrange(dimm)]
    i_index = xrange(len(s_table))
    j_index = xrange(len(s_table[0]))
    if (incr == 'k'): # kill increases
        for i in i_index:
            for j in j_index:
                new_life = constant_lives(l, n + i)
                s_table[i][j] = st.test(n + i, k + j, s, l, p, sf, False)
    if (incr == 's'): # skip increases
        for i in i_index:
            for j in j_index:
                new_life = constant_lives(l, n + i)
                s_table[i][j] = st.test(n + i, k, s + j, l, p, sf, False)
    return s_table

# creates a table of survivors with each row being how many people and col being how many kills/skips
def survivor_table_stc(n = 1, k = 1, s = 1, l = 1, p = 0, sf = False, dimm = 100, incr = 'k'):
    s_table = [[0]*dimm for _ in xrange(dimm)]
    i_index = xrange(len(s_table))
    j_index = xrange(len(s_table[0]))
    if (incr == 'k'): # kill increases
        for i in i_index:
            for j in j_index:
                new_life = constant_lives(l, n + i)
                dead = josephus(n + i, k + j, s, new_life, p, sf)
                dead_st = st.test(n + i, k + j, s, l, p, sf, False)
                if dead_st == -1: s_table[i][j] = -1
                else: s_table[i][j] = int(dead_st - dead[-1]) % (n + i)
    if (incr == 's'): # skip increases
        for i in i_index:
            for j in j_index:
                new_life = constant_lives(l, n + i)
                dead = josephus(n + i, k, s + j, new_life, p, sf)
                dead_st = st.test(n + i, k, s + j, l, p, sf, False)
                if dead_st == -1: s_table[i][j] = -1
                else: s_table[i][j] = int(dead_st - dead[-1]) % (n + i)
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

# used to create table for case l=k=s compared with n and n>=2k both increase
def survivor_table_2(dimm = 100):
    s_table = [[0]*dimm for _ in xrange(dimm)]
    i_index = xrange(len(s_table))
    j_index = xrange(len(s_table[0]))
    for i in i_index:
        for j in j_index:
            if (i >= (2 * j)) and (i > 0) and (j > 0):
                new_life = constant_lives(j, i)
                dead = josephus(i,j,j, new_life, 0)
                s_table[j][i] = dead[-1] + 1
    return s_table

def create_csv(table, fn):
    with open(fn + '.csv', 'wb') as myfile:
        wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
        for i in table: wr.writerow(i)

if __name__ == '__main__':
    # (numb, kill, skip, life, stpt) = game_parameters()
    # (dimm, incr) = table_parameters()
    # filename = raw_input("Filename: ")
    # create_csv(survivor_table(numb, kill, skip, life[0], stpt, dimm, incr), filename)
    # create_csv(survivor_table(1, 1, 2, 1, 0, 200, "k"), "such200")
    # create_csv(survivor_table_st(1, 1, 2, 1, 0, True, 100, "k"), "q2-2-100-mk2mk1comp")
    # create_csv(survivor_table_stt(1, 1, 3, 1, 0, True, 100, "k"), "q2-3-100-t-m")
    # create_csv(survivor_table_stc(1, 1, 2, 1, 0, True, 100, "k"), "q2-2-100-mk2mk1comp-c")
    # create_csv(survivor_table_2(), filename)
