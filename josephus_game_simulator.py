# simulates the Ducks and Geese Josephus Game
# for those who do not want to use the comman line arguments or need to input custom lives per player
# (c) 2017 David Ariyibi, Williams College, daa1@williams.edu

from josephus import josephus, input_lives, constant_lives

# commant line interface for assigning parameters
def game_parameters():
    while True:
        numb = int(raw_input("Number of players: "))
        if numb > 0: break

    while True:
        kill = int(raw_input("Number of players shot in a row: "))
        if kill > 0: break

    while True:
        skip = int(raw_input("Number of players skipped in a row: "))
        if skip > -1: break

    while True:
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
        if stpt == stpt % numb: break

    while True:
        kfsf = raw_input("Skip-first/kill-first ('s' or 'k'): ")
        if kfsf == "s":
            kfsf = True
            break
        elif kfsf == "k":
            kfsf = False
            break

    while True:
        graf = raw_input("Graphic? ('y' or 'n'): ")
        if graf == "y":
            graf = True
            break
        if graf == "n":
            graf = False
            break

    return numb, kill, skip, life, stpt, kfsf, graf

if __name__ == '__main__':
    numb, kill, skip, life, stpt, kfsf, graf = game_parameters()
    print "Order of death: " + str(josephus(numb, kill, skip, life, stpt, kfsf, graf))
