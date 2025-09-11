#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSmallestMissingPositive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY orderNumbers as parameter.
#

def findSmallestMissingPositive(orderNumbers):
    onlyPositive = sorted([number for number in orderNumbers if number > 0])
    # tiro todos números negativos e o zero pois esse não me interessam
    
    if len(onlyPositive) == 0:
        return 1 # se a lista estiver vazia retorno 1
    else: # senão
        for i in range(1, (onlyPositive[-1]) + 1): # percorro a lista
            if i == (onlyPositive[-1]): # se o i for igual ao último elemento a lista chegou ao final
                return (onlyPositive[-1]) + 1 # então o menor que falta é o último elemento mais um
            if i not in onlyPositive: # se um número não está na lista
                return i # então ele é o que falta

if __name__ == '__main__':
    orderNumbers_count = int(input().strip())

    orderNumbers = []

    for _ in range(orderNumbers_count):
        orderNumbers_item = int(input().strip())
        orderNumbers.append(orderNumbers_item)

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
