#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby



if __name__ == '__main__':
    s = ''.join(sorted(input()))
    s = [[str(key), len(list(group))] for key, group in groupby(s)]
    s = sorted(s, key=lambda x: x[1], reverse=True)
    s = s[0:3]
    for item in s:
        print(item[0], item[1])
