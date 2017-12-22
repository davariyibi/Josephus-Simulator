# program simulates a variation of Josephus Problem
# (c) 2017 David Ariyibi, Williams College, daa1@williams.edu

import csv

numb = 0
kill = 0
skip = 0
life = []
stpt = 0

# interface for assigning parameters for game
def param():
    numb = int(raw_input("Number of people: "))
    kill = int(raw_input("Number of people shot in a row: "))
    skip = int(raw_input("Number of people skipped in a row: "))
    ques = raw_input("Same number of lives per person? ('y' or 'n'): ")
    if (ques == 'y'):
        life = constant_lives(int(raw_input("Number of lives per person: ")), n)
    elif (ques == 'n'):
        life = input_lives(n)
    stpt = int(raw_input("Who do you want to start with?: ")) - 1

# all people in game have the same number of lives
def constant_lives(i, n):
    array = []
    for j in xrange(n):
        array.append(i)
    return array

# user decides the life amount for each person
def input_lives(n):
    array = [0] * n
    for i in xrange(n):
        array[i] = int(raw_input("Number of lives for person " + str(i + 1) + ": "))
    return array

# runs a Josephus Problem game given num of people, kill length, skip length, lives per person, and start-point
def josephus(n, k, s, l, p = 0):
    totalLives = sum(l)
    deadList = [] # list of people dead
    person = p % n # starts at given start-point
    success = False
    while (totalLives is not 0):
        for i in range(k): # process of killing people
            if (totalLives is not 0): # stops an infinite loop of all dead people
                success = False # for crossing people who already died
                while not success:
                    person = person % n # keeps person pointer from going out of bounds
                    lives = l[person]
                    if (lives > 0):
                        lives = lives - 1 # person loses a life
                        totalLives = totalLives - 1
                        l[person] = lives # updates person's life amount
                        success = True
                        if (lives is 0): # if person is dead, adds them to deadList
                            deadList.append(person + 1)
                    person = person + 1 # moves on to next person
        for j in range(s): # process of skipping people
            if (totalLives is not 0):
                success = False
                while not success:
                    person = person % n
                    if (l[person] > 0):
                        success = True
                    person = person + 1
    return deadList

# finds placement of survivor in cases of k = 1 and l = 1
# equation: 'f(n,k) = ((f(n - 1,k) + k - 1) mod(n)) + 1, with f(1,k) = 1' (c) Wikipedia/Josephus_problem
# must subtract s from return value since it's skip-first
# must add 1 to s-input value since it accounts for a kill at s + 1 position
def survivor_k1l1(n, s):
    if (n is 1):
        return 1
    elif (n > 1):
        return ((survivor_k1l1(n - 1, s) + s - 1) % n) + 1
    else:
        return 0

def survivor_l1(n, k, s):
    if (n is 1):
        return 1
    elif (n > 1):
        return ((survivor_k1l1(n - k, s) + s - 1) % n) + 1
    else:
        return 0

def test(n, k, s, l, p):
    print 'josephus: ' + str(josephus(n, k, s, l, p))
    if (k is 1):
        print 's_k1l1:   ' + str(survivor_k1l1(n, s + 1) - s)
    print 's_l1:     ' + str(survivor_l1(n, k, s + 1) - s)

# creates a table of survivors with each row being how many people and col being how many kills/skips
def survivor_table(n = 1, k = 1, s = 1, l = 1, p = 0, dim = 100, texas = True):
    s_table = [[0]*dim for _ in xrange(dim)]
    i_index = xrange(len(s_table))
    j_index = xrange(len(s_table[0]))
    if (texas): # kill increases
        for i in i_index:
            for j in j_index:
                new_life = constant_lives(l, n + i)
                dead = josephus(n + i, k + j, s, new_life, p)
                s_table[i][j] = dead[-1]
    else: # skip increases
        for i in i_index:
            for j in j_index:
                new_life = constant_lives(l, n + i)
                dead = josephus(n + i, k, s + j, new_life, p)
                s_table[i][j] = dead[-1]
    return s_table

# creates a table of survivors with each row being how many people and col being how many kills/skips
def survivor_table_2(n = 1, k = 1, s = 1, l = 1, p = 0, dim = 100, texas = True):
    s_table = [[0]*dim for _ in xrange(dim)]
    i_index = xrange(len(s_table))
    j_index = xrange(len(s_table[0]))
    if (texas): # kill increases
        for i in i_index:
            for j in j_index:
                new_life = constant_lives(l + j, n + i)
                dead = josephus(n + i, k + i, s, new_life, p)
                s_table[i][j] = dead[-1]
    else: # skip increases
        for i in i_index:
            for j in j_index:
                new_life = constant_lives(l, n + i)
                dead = josephus(n + i, k, s + j, new_life, p)
                s_table[i][j] = dead[-1]
    return s_table

def josephus_to_csv(event_list, filename):
    with open(filename + '.csv', 'wb') as myfile:
        wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
        for i in event_list:
            wr.writerow(i)

if __name__ == '__main__':
    # param()
    # print "List of people in order of death: " + str(josephus(numb, kill, skip, life))
    # test(13, 2, 4, [1,1,1,1,1,1,1,1,1,1,1,1,1], 0)
    # josephus_to_csv(express(numb, kill, skip, life, 1, 0), 'test')

    josephus_to_csv(survivor_table_2(n = 2, k = 1, s = 4), 'survivor_table_s4nequkplus1100')
# (n, k, s, l, p = 0)
    # print josephus(10,9,3,constant_lives(5,10),0)








# we shoot first insteaed of skip first because pattern is the same, just adding the number of initial skips

# creates numbertr of iterations of a josephus game with slightly different parameters
# choice: 0 = increase kill, 1 = increase skips, 2 = increase lives
# only works if lives are constant
# def express(n, k, s, l, iter, choice):
#     event_list = []
#     for i in range(iter):
#         if choice is 0:
#             event = str(josephus(n, k + i, s, l))
#             event_list.append((n, k + i, s, l[0], event))
#             print event
#         elif choice is 1:
#             event = str(josephus(n, k, s + i, l)
#             event_list.append((n, k, s + i, l[0], event))
#             print event
#         elif choice is 2:
#             event = str(josephus(n, k, s + i, constant_lives(l[0] + i, n)))
#             event_list.append((n, k, s, l[0], event))
#             print event
#     return event_list[1:]
