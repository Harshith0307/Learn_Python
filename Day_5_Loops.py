#print the 10 lines of the multiplication tables

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    i = 1
    while 1 <= i <= 10:
        print(n,"x", i,"=",n*i)
        i = i + 1