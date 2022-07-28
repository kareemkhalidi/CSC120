'''File: sqeuence_len.py.
   Author: Kareem Khalidi.
   Purpose: Takes string of integers and 
            counts how many are in order.
   Course: CSC 120 1st Semester.
'''

def main():

    flag = True
    inputList = []
    isIncreasing = True
    flag2 = True


    while(flag):
        currentLine = input().split()
        for i in range(len(currentLine)):
            inputList.append(int(currentLine[i]))
        if(len(inputList) >= 2 & flag2):

            for i in range(len(inputList) - 1):
                if(inputList[i] > inputList[i + 1]):
                    isIncreasing = False
                    flag2 = False
                    break
                elif(inputList[i] < inputList[i + 1]):
                    flag2 = False
                    break
            
            if(isIncreasing):
                for i in range(len(inputList) - 1):
                    if(inputList[i + 1] < inputList[i]):
                        print(i + 1)
                        flag = False
                        break
            else:   
                for i in range(len(inputList) - 1):
                    if(inputList[i + 1] > inputList[i]):
                        print(i + 1)
                        flag = False
                        break        

if __name__ == "__main__":
    main()