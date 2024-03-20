#!/bin/python3

import math
import os
import random
import re
import sys

def viralAdvertising(n):
    # Write your code here
    initial_adv = 5
    initial_like = 2
    cum_like = initial_like
    for day in range(2,n+1):
        floor_value = math.floor(initial_adv/2)
        initial_adv = floor_value*3
        initial_like = math.floor(initial_adv/2)
        cum_like += initial_like
    return cum_like
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
