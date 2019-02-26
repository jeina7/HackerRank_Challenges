# Hackerrank 10 Days of Statistics Challenge
# https://www.hackerrank.com/domains/tutorials/10-days-of-statistics
# Day 6

import math

X = int(input())
N = int(input())
mean = float(input())
std = float(input())

mean = N * mean
std = (N ** 0.5) * std

def norm_cdf(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

print(round(norm_cdf(X, mean, std), 4))
