def main():
    u = input().split()
    u2 = input().split()
    print("The first line was: " + str(u))
    print("The second line was: " + str(u2))
    print()
    combinedList = u + u2
    print("The combination of both lines had " + str(len(combinedList)) 
    + " words.")
    print("The combined set of words was: " + str(combinedList))
    combinedList.sort()
    print()
    print("After sorting, the words were: " + str(combinedList))
    print()
    print("Pairs:")
    for i in range(min(len(u), len(u2))):
        print(str(i) + ": " + u[i] + "," + u2[i])

main()