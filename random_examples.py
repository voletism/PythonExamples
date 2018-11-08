import os
import random
import time

for i in range(10):
    print(random.random())

print(24* "*")

# random numbers between 3 and 7 ; this means > 3 < 7
def randum():
    return (4*random.random() + 3)

for i in range(10):
    print(randum())

# use uniform function for the same
print(24* "*")
for i in range(10):
    print(random.uniform(3,7))

#rolling the dice (between 1 to 6)
print(24* "*")
for i in range(10):
    print(random.randint(1,6))

# rock, paper and scissors

game = ["rock", "paper", "scissors"]
print(24* "*")
for i in range(10):
    print(random.choice(game))


def primeNumber(number):
    if number == 1:
        return False # 1 is not a prime number

    if number == 2:
        return True

    if number > 2 and number % 2 ==0:
        return False

    for d in range(2, number):
        if number % d == 0:
            return False
    #print(number)
    return True

#==============TIme Function=============

t0 = time.time()
for n in range (1, 1000):
    primeNumber(n)
t1 = time.time()
print("time required", t1 - t0)

#==============random walks===================

def random_walks(n):
    # Return coordinates after 'n' blocks
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(["N", "S", "E", "W"])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x + 1
        else :
            x = x - 1
    return(x, y)

def random_walk_2(number):
    x, y = 0,0
    for i in range(number):
        # choice for north, south, east, west
        (dx, dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy

    return(x,y)

walk = random_walks(10)
print(walk, "distance from home= ",
      abs(walk[0]) + abs(walk[1]))

walk = random_walk_2(10)
print(walk, "distance from home= ",
      abs(walk[0]) + abs(walk[1]))



