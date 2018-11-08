#/user/bin/python3
import re
import sys

str = "this is string example....wow!!!"
mylist = str.split( )
for string in mylist:
    print(string, end =' ')
    print(" ")

print (str.split('i',2))
print (str.split('w'))

string = "this is how, we  test coders. with outmost! interest and skills? x y z"
listStrings = string.split('?')
count = []
for sentence in listStrings:
    print(sentence)
    words = sentence.split()
    count.append(len(words))

count.sort()
print(count[-1])
print(count)


string = "this is how, we  test coders? with   outmost! interest and skills? x y z"
listStrings = re.split('[?,.]', string)
count = []
for sentence in listStrings:
    print(sentence)
    words = sentence.split()
    count.append(len(words))

print(words)
count.sort()
print(count[-1])