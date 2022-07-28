'''File: count_items.py.
   Author: Kareem Khalidi.
   Purpose: Reads file of keys and numbers,
            combines values with the same key
            together, and sorts and prints them.
   Course: CSC 120 1st Semester.
'''

import os

def main():

    this_script   = os.path.realpath(__file__)
    dir_of_script = os.path.dirname(this_script)
    os.chdir(dir_of_script)

    u = input("File to scan: ")
    f = open(u, 'r')
    keys = []
    values = []

    for line in f:
        line = line.strip()
        if(len(line) > 0):
            if(line[0] != "#"):
                temp = line.split()
                if(temp[0] in keys):
                    a = keys.index(temp[0])
                    values[a] = values[a] + int(temp[1])
                else:
                    keys.append(temp[0])
                    values.append(int(temp[1]))

    
    fileDict = dict(zip(keys, values))
    keys.sort()
    listOfTuples = []
    print("STEP 1: THE ORIGINAL DICTIONARY")
    for i in range(len(keys)):
        currentKey = keys[i]
        currentValue = fileDict[currentKey]
        listOfTuples.append((currentValue, currentKey))
        print("  Key: " + currentKey + " Value: " + str(currentValue))

    print()
    print("STEP 2: A LIST OF VALUE->KEY TUPLES")
    print(listOfTuples)

    listOfTuples.sort()
    print()
    print("STEP 3: AFTER SORTING")
    print(listOfTuples)

    print()
    print("STEP 4: THE ACTUAL OUTPUT")
    for i in range(len(listOfTuples)):
        print(listOfTuples[i][1] + " " + str(listOfTuples[i][0]))

if __name__ == "__main__":
    main()