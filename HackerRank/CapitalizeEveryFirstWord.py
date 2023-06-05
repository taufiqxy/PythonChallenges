#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # set string to lower and convert it into list
    s = list(s.lower())
    
    # upper first character in string
    s[0] = s[0].upper()
    
    # convert first character after withspace to upper case
    for i in range(0,len(s)):
        if (s[i].isspace() and not s[i+1].isspace()):
            s[i+1] = s[i+1].upper()
    
    # join list
    return ''.join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
