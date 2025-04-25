#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):    
    #Sort the array
    arr.sort()
    
    #Find min sum
    min_sum = 0
    for i in range(0, 4):
        min_sum += arr[i]
        
    #Find max sum
    max_sum = 0
    for i in range(1, 5):
        max_sum += arr[i]
    
    print(str(min_sum) + " " + str(max_sum))
    
    #Time Complexity: O(nlogn) + O(n - 1) => O(n) where n = 5
    #Space Complexity: O(1)
