#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    n = len(grid)
    
    #Go through all the rows and rearrage them in ascending order if needed
    for i in range(n):
        row = grid[i]
        temp = []
        for letter in row:
            temp.append(letter)
        temp.sort()
        if row != temp:
            new_row = ''
            for letter in temp:
                new_row += letter
            grid[i] = new_row
        
    #Now check if columns are sorted
    for i in range(n):
        column = []
        for row in grid:
            column.append(row[i])
        sorted_column = column.copy()
        sorted_column.sort()
        if column != sorted_column:
            return "NO"
    
    return "YES"
