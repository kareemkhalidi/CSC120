import os

def main():

    this_script   = os.path.realpath(__file__)
    dir_of_script = os.path.dirname(this_script)
    os.chdir(dir_of_script)

    print("Please give the name of the obstacles filename, or - for none:")
    obstacles = False

    while(True):
        f = input()
        if(f.strip() == "-"):
            break
        elif(len(f.strip()) == 0):
            print("ERROR: The obstacle filename is blank")
        else:
            try:
                f = open(f)
                obstacles = True
                break
            except:
                print("ERROR: The obstacle filename doesn't exist")
    
    if(obstacles):
        f = f.read().split("\n")
        for i in range(f.count('')):
            f.remove('')
        for i in range(len(f)):
            tempList = f[i].split()
            tempList[0] = int(tempList[0])
            tempList[1] = int(tempList[1])
            f[i] = tuple(tempList)
        f = set(f)
    else:
        f = {}

    twine = [(0, 0)]

    while(True):

        print("Current position: " + str(twine[len(twine) - 1]))
        print("Your history:     " + str(twine))
        print("What is your next command?")
        try:
            u = input().lower().strip()
        except:
            break

        if(len(u.split()) > 1):
            print("ERROR: Commands are one word only.\n")
        elif(len(u) == 0):
            print("You do nothing.\n")
        elif(u == "n"):
            twine.append((twine[-1][0], twine[-1][1] + 1))
            if(set(twine).isdisjoint(f)):
                print()
            else:
                twine.pop()
                print("You could not move in that direction, " 
                + "because there is an obstacle in the way.")
                print("You stay where you are.\n")
        elif(u == "e"):
            twine.append((twine[-1][0] + 1, twine[-1][1]))
            if(set(twine).isdisjoint(f)):
                print()
            else:
                twine.pop()
                print("You could not move in that direction, " 
                + "because there is an obstacle in the way.")
                print("You stay where you are.\n")
        elif(u == "s"):
            twine.append((twine[-1][0], twine[-1][1] - 1))
            if(set(twine).isdisjoint(f)):
                print()
            else:
                twine.pop()
                print("You could not move in that direction, " 
                + "because there is an obstacle in the way.")
                print("You stay where you are.\n")
        elif(u == "w"):
            twine.append((twine[-1][0] - 1, twine[-1][1]))
            if(set(twine).isdisjoint(f)):
                print()
            else:
                twine.pop()
                print("You could not move in that direction, " 
                + "because there is an obstacle in the way.")
                print("You stay where you are.\n")
        elif(u == "back"):
            if(len(twine) > 1):
                twine.pop()
                print("You retrace your steps by one space\n")
            else:
                print("Cannot move back, as you're at the start!\n")
        elif(u == "crossings"):
            print("There have been " + str(twine.count(twine[-1])) + 
            " times in the history when you were at this point.\n")
        elif(u == "map"):
            print("+-----------+")
            for i in range(11):
                s = "|"
                for j in range(11):
                    if(twine[-1] == (j - 5, (i - 5) * -1)):
                        s += "+"
                    elif(i - 5 == 0 and j - 5 == 0):
                        s += "*"
                    elif(twine.count((j - 5, (i - 5) * -1)) > 0):
                        s += "."
                    elif(not({(j - 5, (i - 5) * -1)}.isdisjoint(f))):
                        s += "X"
                    else:
                        s += " "
                print(s + "|")
            print("+-----------+")
        elif(u == "ranges"):
            biggestN = 0
            biggestE = 0
            biggestS = 0
            biggestW = 0
            for i in range(len(twine)):
                if(twine[i][0] > biggestE):
                    biggestE = twine[i][0]
                if(twine[i][0] < biggestW):
                    biggestW = twine[i][0]
                if(twine[i][1] > biggestN):
                    biggestN = twine[i][1]
                if(twine[i][1] < biggestS):
                    biggestS = twine[i][1]
            print("The furthest West your twine goes is " + str(biggestW))
            print("The furthest East your twine goes is " + str(biggestE))
            print("The furthest South your twine goes is " + str(biggestS))
            print("The furthest North your twine goes is " + str(biggestN))
            print()
        else:
            print("ERROR: Unfamiliar command.\n")

if __name__ == "__main__":
    main()