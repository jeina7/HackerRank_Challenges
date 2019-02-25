# Hackerrank 10 Days of Statistics Challenge
# https://www.hackerrank.com/domains/tutorials/10-days-of-statistics
# Day 5

import math

mean, std = list(map(int, input().split()))
a = float(input())
b, c = list(map(float, input().split()))

def norm_cdf(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

print(round(norm_cdf(a, mean, std), 3))
print(round(norm_cdf(c, mean, std) - norm_cdf(b, mean, std), 3))
