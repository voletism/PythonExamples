import os
import sys
import hashlib

def basictype():
    abc_list = [1,2,3,4,5,6,7,8,9,10]
    abc_tuple = (11,12,13,14)

    number = 19
    floating = float(number)
    print("number=", number,"floating=", floating)

    list_new = list(abc_tuple)

    print(list_new)
    return

def bubblesort():
    array = [12,6,34,56,98,42,8,10,1,102, 89, 69,7]
    length = len(array)

    for i in range(0,length):
        for j in range(0,length-1):
            if ( array[j] > array[j+1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

    print(array)
    print("Largest number = {}".format(array[-1]))
    print("Second Largest number = {}".format(array[-2]))
    return

def amstrong():
    # take input from the user
    number = int(input("Enter a number: "))
    # initialize sum
    sum = 0
    # find the sum of the cube of each digit
    temp = number
    print(number)

    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
       # dividing number by 10 and return rounded number without decimals
    print(sum)

    # display the result
    if number == sum:
       print(number,"is an Armstrong number")

    else:
       print(number,"is not an Armstrong number")

def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename, 'rb') as file:
       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()


def checkStringInFile():
    found = False
    string = "BaBu"
    string = string.lower()
    try:

        with open('example.txt', 'r') as outfile:
            line = outfile.read()
            if string in line:
                found = True
                print("found the string {}" .format(string))
        return found
    except:
         print(FileNotFoundError)

def isPalindrome(string):
    length = len(string)

    # Run loop from 0 to len/2
    for i in range(0, int(length/2)):
        if string[i] != string[length - i - 1]:
            return False
    return True

def checkMultipleOccurances():
    text = 'Allowed Hello Hollow'
    index = 0
    while index < len(text):
        index = text.find('ll', index)
        if index == -1:
            break
        print('ll found at', index)
        index += 2  # +2 because len('ll') == 2
    try:
        with open('example.txt', 'r') as outfile:
            line = outfile.read()
            index = 0
            while index < len(line):
                index = line.find('babu', index)
                if index == -1:
                    break
                print("found the string {}" .format(index))
                index = index + len('babu')
    except:
         print(FileNotFoundError)

    return

def main():

    bubblesort()

    found = checkStringInFile()
    if found:
        print("true")
    else:
        print("false")

    # main function
    string = "malayalam"
    answer = isPalindrome(string)
    if (answer):
        print("Yes it is Palindrome")
    else:
        print("No it is not Palindrome")

    # message = hash_file("track1.mp3")
    message = hash_file("example.txt")
    print(message)

    checkMultipleOccurances()

    basictype()

    amstrong()

    return

if __name__ == "__main__":
    main()