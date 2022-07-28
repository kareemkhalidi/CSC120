from utils import *
import os

def main():

    this_script   = os.path.realpath(__file__)
    dir_of_script = os.path.dirname(this_script)
    os.chdir(dir_of_script)

    fileName = input("file: ")
    n = int(input("n: "))

    f = open(fileName, "r")
    fileData = read_file(f)

    print("--- SONG LIST ---")
    for i in range(len(fileData)):
        songId = str(fileData[i][0])
        songInfo = fileData[i][1]
        songNotes = str(fileData[i][2])
        print("id=" + songId + " info=\"" + songInfo + "\" notes=" + songNotes)
    print()

    print("--- COMPARISONS ---")
    similarityOfMS = compare_melodies(fileData[0][2], fileData[1][2], n)
    indexOfMs = 1
    q = str(fileData[0][0])
    w = str(fileData[1][0])
    print("id_a=" + q + " id_b=" + w + " similarity=" + str(similarityOfMS))
    for i in range(len(fileData) - 2):
        tempSim = compare_melodies(fileData[0][2], fileData[i + 2][2], n)
        if(tempSim > similarityOfMS):
            similarityOfMS = tempSim
            indexOfMs = i + 2
        w = str(fileData[i + 2][0])
        print("id_a=" + q + " id_b=" + w + " similarity=" + str(tempSim))

    print()

    print("--- RESULT ---")
    print("Most similar songs:")
    print("  " + fileData[0][1])
    print("  " + fileData[indexOfMs][1])
    print()

    print("  ids: " + str(fileData[0][0]))
    print("  ids: " + str(fileData[indexOfMs][0]))
    print()

    print("Melodies:")
    melodyString = "  "
    for i in range(len(fileData[0][2])):
        melodyString += fileData[0][2][i] + " "
    print(melodyString)
    melodyString = "  "
    for i in range(len(fileData[indexOfMs][2])):
        melodyString += fileData[indexOfMs][2][i] + " "
    print(melodyString)
    print()

    print("Set 1")
    slicedData = get_slices(fileData[0][2], n)
    for i in range(len(slicedData)):
        slicedData[i] = tuple(slicedData[i])
    slicedData = list(dict.fromkeys(slicedData))
    slicedData.sort()
    for i in range(len(slicedData)):
        tempString = "  "
        for j in range(n - 1):
            tempString += slicedData[i][j] + " "
        tempString += slicedData[i][n - 1]
        print(tempString)
    print()

    print("Set 2")
    slicedData = get_slices(fileData[indexOfMs][2], n)
    for i in range(len(slicedData)):
        slicedData[i] = tuple(slicedData[i])
    slicedData = list(dict.fromkeys(slicedData))
    slicedData.sort()
    for i in range(len(slicedData)):
        tempString = "  "
        for j in range(n - 1):
            tempString += slicedData[i][j] + " "
        tempString += slicedData[i][n - 1]
        print(tempString)

main()