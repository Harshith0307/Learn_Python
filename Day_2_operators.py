#!/bin/python3

import math
import os
import random
import re
import sys

# Calculate the toatal meal price based on the subtotal, tip percentage, and tax percentage
def solve(meal_cost, tip_percent, tax_percent):
    tip_price = 0
    tax_price = 0

    tax_price = meal_cost*(tax_percent/100)
    tip_price = meal_cost*(tip_percent/100)

    result = meal_cost + tip_price + tax_price
    result = round(result)
    print(result)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)

