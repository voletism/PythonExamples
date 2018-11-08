import random
import time

names = ["James", "Lucy", "Kevin", "Eastwood", "Tom Hanks", "Ethen Hunt", "Alica", "Silverstone"]
majors = ["Maths", "Science", "Social", "Biology", "English", "Finnish"]

# A simple generator for Fibonacci Numbers
def fibinocci(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b

    # Create a generator object

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id':i,
            'name':random.choice(names),
            'major':random.choice(majors)
        }
        result.append(person)

    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

def main():
    t1 = time.clock()
    people = people_list(1000)
    #print(people)
    t2 = time.clock()
    print("Time in list{} seconds ".format(t2 - t1))

    t3 = time.clock()
    #generator holds only one object at a time.
    person = people_generator(1000)
    t4 = time.clock()
    print("Time in generator{} seconds ".format(t4-t3))
    print(next(person))

    x = fibinocci(5)
    # Iterating over the generator object using next
    # In Python 3, __next__()
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())

if __name__ == "__main__":
    main()
