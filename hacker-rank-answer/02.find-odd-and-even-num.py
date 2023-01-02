#!/bin/python3
import math
import os
import random
import re
import sys

# Given an integer, n, perform the following conditional actions:
# if n is odd, print Weird
# if n is even and in the inclusive range of 2 to 5, print Not Weird
# if n is even and in the inclusive range of 6 to 20, print weird
# if n is even and greater than 20, print weird

if __name__ == '__main__':
    n = int(input("please enter your number: ").strip())

# condition for even numbers
if n % 2 == 0:
        if 2 < n < 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")
# condition for add numbers
elif n % 2 != 0:
    print("Weird")