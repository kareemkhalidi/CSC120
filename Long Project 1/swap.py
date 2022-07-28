'''File: swap.py.
   Author: Kareem Khalidi.
   Purpose: Takes input string and swaps
            first and second halves.
   Course: CSC 120 1st Semester.
'''

def main():
    uIn = input("Please give a string to swap: ").strip()
    isEven = False
    if(len(uIn) % 2 == 0):
        isEven = True
    halfLen = int(len(uIn)/2)
    firstHalf = uIn[:halfLen]
    lastHalf = ""
    middle = ""
    if(isEven):
        lastHalf = uIn[halfLen:]
    else:
        lastHalf = uIn[halfLen + 1:]
    if(not(isEven)):
        middle = uIn[halfLen]
    print(lastHalf + middle + firstHalf)

if __name__ == "__main__":
    main()