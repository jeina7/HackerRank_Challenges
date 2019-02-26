# Hackerrank 10 Days of Statistics Challenge
# https://www.hackerrank.com/domains/tutorials/10-days-of-statistics
# Day 5

import math

mean, std = list(map(int, input().split()))
a = int(input())
b = int(input())

def norm_cdf(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

print(round((1 - norm_cdf(a, mean, std)) * 100, 2))
print(round((1 - norm_cdf(b, mean, std)) * 100, 2))
print(round(norm_cdf(b, mean, std) * 100, 2))
