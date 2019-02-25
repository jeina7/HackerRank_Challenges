# Hackerrank 10 Days of Statistics Challenge
# https://www.hackerrank.com/domains/tutorials/10-days-of-statistics
# Day 5

import math

lambda_ = float(input())
k = int(input())

def factorial(k):
    if k == 1:
        return k
    else:
        return factorial(k-1) * k

print(round((lambda_ ** k) * math.exp(-lambda_) / factorial(k), 3))
