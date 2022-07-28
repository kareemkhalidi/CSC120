'''File: population.py.
   Author: Kareem Khalidi.
   Purpose: Reads file of states and populations
            and performs calculations on the data.
   Course: CSC 120 1st Semester.
'''

import os

def main():
    this_script   = os.path.realpath(__file__)
    dir_of_script = os.path.dirname(this_script)
    os.chdir(dir_of_script)
    
    uIn = input("file: ").strip()
    f = open(uIn, 'r')
    storageList = []
    totalPop = 0
    for line in f:
        line = line.strip()
        if(len(line) > 0):
            if(line[0] != "#"):
                if(not(line.isspace())):
                    storageList.append(line.strip("\n"))
    for i in range(len(storageList)):
        tempList = storageList[i].split()
        countryName = ""
        for j in range(len(tempList) - 1):
            countryName += tempList[j]
            countryName += " "
        countryName = countryName.strip()
        print("State/Territory: " + countryName)
        print("Population: " + tempList[len(tempList) - 1])
        totalPop += int(tempList[len(tempList) - 1])
        print()
    print("# of States/Territories: " + str(len(storageList)))
    print("Total Population: " + str(totalPop))

if __name__ == "__main__":
    main()