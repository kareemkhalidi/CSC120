'''File: bob.py.
   Author: Kareem Khalidi.
   Purpose: Find all palindromes from a list of words
   Course: CSC 120 1st Semester.
'''

import os

def remove_alpha(data):
    '''Summary: removes all non alpabetical chars
                from a string
       Arguments: data (string)
       Returns: data (string without alpha chars)
       Assumptions: None
       Nothing else of interest
    '''
    while data.count("\n") > 0:
        data = data.replace("\n", " ")

    i = 0
    while i < len(data):
        if not data[i].isalpha() and data[i] != " ":
            data = data.replace(data[i], "")
        i += 1
    return(data)


def remove_s_less_than_2(data):
    '''Summary: removes all elements from array with len < 2
       Arguments: data (array)
       Returns: data (array without elements len < 2)
       Assumptions: None
       Nothing else of interest
    '''
    i = 0
    while i < len(data):
        if len(data[i]) < 2:
            data.pop(i)
            i -= 1
        i += 1
    return(data)

def print_one_word_palindromes(data):
    '''Summary: prints palindromes located in the provided array
       Arguments: data (array of strings)
       Returns: None
       Assumptions: None
       Nothing else of interest
    '''
    simple_pal_set = set()
    for i in range(len(data)):
        if data[i] == data[i][::-1]:
            simple_pal_set.add(data[i])
    simple_pal_array = list(simple_pal_set)
    simple_pal_array.sort()
    print("1-WORD PALINDROMES:")
    for i in range(len(simple_pal_array)):
        print("  " + simple_pal_array[i])
    print()

def print_two_and_three_word_palindromes(data):
    '''Summary: combines words in the array to find palindromes
       Arguments: data (array of string)
       Returns: None
       Assumptions: None
       Nothing else of interest
    '''
    complex_pal_set = set()
    for i in range(len(data)):
        for j in range(len(data)):
            #if i != j:
            temp_string = data[i] + data[j]
            if temp_string == temp_string[::-1]:
                complex_pal_set.add(temp_string)
    for i in range(len(data)):
        for j in range(len(data)):
            for k in range(len(data)):
                temp_string = data[i] + data[j] + data[k]
                if temp_string == temp_string[::-1]:
                    complex_pal_set.add(temp_string)
    complex_pal_array = list(complex_pal_set)
    complex_pal_array.sort()
    print("2-WORD AND 3-WORD PALINDROMES:")
    for i in range(len(complex_pal_array)):
        print("  " + complex_pal_array[i])
    print()

def print_many_word_palindromes(in_data, dump):
    '''Summary: prints palindromes of any length
       Arguments: in_data (array of strings),
                  dump (len of longest allowed palindrome)
       Returns: None
       Assumptions: None
       Nothing else of interest
    '''
    data = []
    for i in range(dump):
        data.append(set())
    for i in range(len(in_data)):
        if len(in_data[i]) <= dump:
            data[len(in_data[i]) - 1].add(in_data[i])
    for i in range(len(data)):
        temp_array = list(data[i])
        for j in range(len(temp_array)):
            if temp_array[j] != temp_array[j][::-1]:
                for k in range(len(in_data)):
                    temp_string = temp_array[j] + in_data[k]
                    if len(temp_string) <= dump and in_data[k] != in_data[k][::-1]:
                        data[len(temp_string) - 1].add(temp_string)

    for i in range(len(data)):
        print("PALINDROMES OF LENGTH " + str(i + 1) 
        + "    - length of candidate list: " + str(len(list(data[i]))))
        temp_array = list(data[i])
        temp_array.sort()
        for j in range(len(temp_array)):
            if temp_array[j] == temp_array[j][::-1]:
                print(temp_array[j])
        print()

def print_word_list(data):
    '''Summary: prints all words in the input file, after filtering
       Arguments: data (array of words)
       Returns: None
       Assumptions: None
       Nothing else of interest
    '''
    temp_set = set(data)
    data = list(temp_set)
    data.sort()
    print("WORD LIST:")
    for i in range(len(data)):
        print("  " + data[i])

def main():
    '''Summary: main method
       Arguments: None
       Returns: None
       Assumptions: None
       Nothing else of interest
    '''
    this_script   = os.path.realpath(__file__)
    dir_of_script = os.path.dirname(this_script)
    os.chdir(dir_of_script)

    file_name = input()
    dump = input().lower()
    if dump != "dump":
        dump = int(dump)

    try:
        f = open(file_name, 'r')
        data = f.read().lower()

        data = remove_alpha(data)

        data = data.split()

        data = remove_s_less_than_2(data)

        if(dump != "dump"):
            print_one_word_palindromes(data)
            print_two_and_three_word_palindromes(data)
            print_many_word_palindromes(data, dump)
        else:
            print_word_list(data)

    except:
        print("ERROR: Could not open the input file: " + file_name)

if __name__ == "__main__":
    main()