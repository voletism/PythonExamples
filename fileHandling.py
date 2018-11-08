import os
import sys

def fileWriting():
    # strings
    oceans = ["Pacific", "Atlantic", "Indian", "Arcatic", "Antarctic"]
    with open("hello.txt", "w") as myfile:
        for ocean in oceans:
            myfile.write(ocean)
            myfile.write("\n")
        # no need to close the file; python closes it

    try:
        with open("hello.txt", 'r') as myfile:
            text = myfile.read().split('\n')
            print(text)
    except FileNotFoundError:
            text = None

    # using binary files
    try:
        with open("ganesha.jpg", 'rb') as infile:
            data = infile.read()
        with open("gg.jpg", 'wb') as outfile:
            outfile.write(data)
            print("1", end=" ")

            print("Done")

    except FileNotFoundError:
        text = None
    return

def convertToOthers(decimal):
    print("The decimal value of",decimal,"is:")
    print(bin(decimal),"in binary.")
    print(oct(decimal),"in octal.")
    print(hex(decimal),"in hexadecimal.")

# define a function
def lcm(x, y):
   """This function takes two integers and returns the L.C.M."""
   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

def main():
    lcm(25, 5, )
    convertToOthers(344)
    fileWriting()

    return

if __name__ == "__main__":
    main()