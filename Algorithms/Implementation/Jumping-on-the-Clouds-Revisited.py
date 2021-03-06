#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e =100
    i = k
    while e > 0:
        e -= 1
        if i >= len(c):
            i -= len(c)
        if(c[i] == 1):
            e -= 2
        if(i == 0):
            break        
        i += k
    return e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
