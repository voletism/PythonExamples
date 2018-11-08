#!/usr/bin/env python

import json
import os
import sys
import pickle
import logging
import math
from math import pi

# create and config logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="logging.txt", level=logging.DEBUG,
                    format = LOG_FORMAT)

logger = logging.getLogger()

# test the logger
logger.info("our first message")
logger.debug("this is debug message")
logger.error("this is error message")
logger.critical("this is critical message")
logger.warning("this is warning message")

print(logger.level)

#os.system('ls')

#os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
#os.system('iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080')

#os.system('cat json.txt | jq \'.resources[0].customer.id\'')


def quadratic_formula(a, b, c):
    # ax2+bx+c = 0
    logger.info("quardratic formula({0},{1},{2})".format(a, b, c))

    #compute the discriminate
    logger.debug("# compute the discriminant b2-4ac")
    disc = b**2 - 4*a*c

    #compute the two routes
    logger.debug("# compute the two routes, -b +- sqrt(b**2-4ac)/2*a")
    root1 = (-b + math.sqrt(disc))/ (2*a)
    root2 = (-b - math.sqrt(disc))/ (2*a)

    # Return the roots
    logger.debug("# return the roots")
    return (root1, root2)

temp = quadratic_formula(1, 0, -4)
print(temp)

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("Radius must be non-negative real number")

    if r < 0:
        raise ValueError("R cannot be negative")
    return pi*(r**2)

#test this function
#radii = [2, 0, -3, 2 + 5j, 10]
#message = "Area of circles with radius r = {radius} is {area}."

#for r in radii:
#    area = circle_area(r)
#print(message.format(radius=r, Area=area))


