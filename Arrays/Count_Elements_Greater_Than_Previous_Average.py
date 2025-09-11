#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    if len(responseTimes) <= 1: # se a lista for menor ou igual a um 
        return 0 # retorno zero
    else:
        counter = 0 
        # contador de quantas vezes os elementos são maiores que a média dos anteriores
        average = responseTimes[1]
       # calcula a média
        for i in range(1,len(responseTimes)):
            average = sum(responseTimes[:i])/ i # a media é a soma de todos elementos anteriores dividido pela quantidade de elementos
            if responseTimes[i] > average: # se o elemento atual for maior que a média
                counter += 1 # contador mais um
            
            
        return counter # retorna o contador

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
