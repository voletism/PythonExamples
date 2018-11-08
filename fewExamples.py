def printDictionary():
    my_dict = {"name": "murthy", "age": 35, "address": "jubilee hills", "id": 80849,
               "location": (4567890, 7689310)}
    for key in my_dict.keys():
        print(key)
        values = my_dict[key]
        print(key, "=", values)

    for values in my_dict.values():
        print(values)

    for key, values in my_dict.items():
        print(key, "=", values)

    #pop, popitem, clear (removes all data)

def fibinocci(number):
    a = 0
    b = 1
    sum = 1
    if type(number) not in [int, float]:
        print("number has to be Interger")
        return
    if (number == 1):
        sum = a + b
        print(sum)
    elif (number >= 2):
        count = 0
        while count < number:
            sum = a + b
            a = b
            b = sum
            count +=1
            print(sum, end=" ")
    else:
       # sum = fibinocci(number -1)+ fibinocci(number -2)
        print("what I am I doing")
    return(sum)

def fibinocci_ver2(number):
    a, b = 0,1
    for i in range(0, number):
        print (a)
        a, b = b, a + b

def factorial(number):
    result = 1
    if type(number) not in [int, float]:
        print("number has to be Integer")

    for i in range(1, number +1):
        result *= i

    return (result)

def factors(number):
    result = 1
    if type(number) not in [int, float]:
        print("number should be Integer")

    if (number <= 0) :
        print ("number should be positive and non zero")

    print("The factors of", number, "are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

def printingStars(number):
    for i in range(1, number + 1):
        for j in range(i):
            print("*", end = ' ')
        print(" ")

def fizzbuzz():
    for number in range(1,101):
        if (number % 5 == 0  and number % 3 == 0):
            print("FizzBuzz")

        elif (number % 5 == 0):
            print("Buzz")

        elif (number % 3 == 0):
            print("Fizz")
        else:
            print(number)

def main():
    fizzbuzz()
    result = factorial(5)
    print(result)
    sum = fibinocci(10)
    print(sum)
    printingStars(5)
    result = factors(125)
    print(result)
    return

if __name__ == "__main__":
    main()