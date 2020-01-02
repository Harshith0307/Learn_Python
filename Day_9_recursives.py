#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product


num = int(input())

print(factorial(num))
