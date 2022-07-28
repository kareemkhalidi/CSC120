'''File: strings_and_input.py.
   Author: Kareem Khalidi.
   Purpose: Prints information about an input string.
   Course: CSC 120 1st Semester.
'''

def main():
    inputString = input("input string: ")
    print(len(inputString))
    print(inputString[1])
    print(inputString[:10])
    if(len(inputString) < 5):
        print(inputString)
    else:
        print(inputString[len(inputString) - 5:])
    print(inputString.upper())
    firstChar = inputString[0]
    if(firstChar.lower() == "q" or firstChar.lower() == "w" or 
    firstChar.lower() == "e" or firstChar.lower() == "r" or 
    firstChar.lower() == "t" or firstChar.lower() == "y"):
        print("QWERTY")
    elif(firstChar == "u" or firstChar == "i" or 
    firstChar == "o" or firstChar == "p"):
        print("UIOP")
    elif(firstChar.isalpha()):
        print("LETTER")
    elif(firstChar.isnumeric()):
        print("DIGIT")
    else:
        print("OTHER")
    num1 = int(input())
    num2 = int(input())
    print(num1 * num2)

if __name__ == "__main__":
    main()