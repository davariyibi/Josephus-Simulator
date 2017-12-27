# program simulates the Ducks and Geese Josephus Game
# works for various other variants depending on input
# (c) 2017 David Ariyibi, Williams College, daa1@williams.edu

# interface for assigning parameters for game
def game_parameters():
    while True:
        numb = int(raw_input("Number of players: "))
        if numb > 0:
            break
    while True:
        kill = int(raw_input("Number of players shot in a row: "))
        if kill > 0:
            break
    while True:
        skip = int(raw_input("Number of players skipped in a row: "))
        if skip > -1:
            break
    while True: # in case of wrong input
        ques = raw_input("Same number of lives per player? ('y' or 'n'): ")
        life = []
        if ques == 'y':
            life = constant_lives(int(raw_input("Number of lives per player: ")), numb)
            break
        if ques == 'n':
            life = input_lives(numb)
            break
    while True:
        stpt = int(raw_input("Which player do you want to start with?: "))
        if stpt == stpt % numb:
            break
    return (numb, kill, skip, life, stpt)

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

# simulates the game
# input: num of people, kill length, skip length, lives per person, and start-point
# output: list of players in order of death and optional graphic of how players are killed
def josephus(n, k, s, l, p = 0, show = False):
    total_lives = sum(l)
    show_list = []
    for i in range(n):
        show_list.append(str(i) + ':')
    dead_list = []
    success = False
    b = 0 # runs before the game starts
    while b < p:
        show_list[b] = show_list[b] + " _"
        b = b + 1
    while (total_lives > 0):
        for i in range(k): # process of killing players
            if (total_lives > 0): # stops an infinite loop of all dead players
                success = False # skips players who have already died
                while not success:
                    p = p % n # keeps player pointer from going out of bounds
                    lives = l[p]
                    if (lives > 0):
                        lives = lives - 1 # player loses a life
                        total_lives = total_lives - 1
                        l[p] = lives # updates player's life amount
                        success = True
                        if (lives == 0): # if player is dead, adds them to dead_list
                            dead_list.append(p)
                        show_list[p] = show_list[p] + " X"
                    else:
                        show_list[p] = show_list[p] + " _"
                    p = p + 1 # moves on to next players
        for j in range(s): # process of skipping people
            if (total_lives > 0):
                success = False
                while not success:
                    p = p % n
                    if (l[p] > 0):
                        show_list[p] = show_list[p] + " O"
                        success = True
                    else:
                        show_list[p] = show_list[p] + " _"
                    p = p + 1
    if show:
        for m in show_list:
            print m
    return dead_list

if __name__ == '__main__':
    (numb, kill, skip, life, stpt) = game_parameters()
    print "Order of death: " + str(josephus(numb, kill, skip, life, stpt, True))
