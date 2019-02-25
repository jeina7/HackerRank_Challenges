# Hackerrank 10 Days of Statistics Challenge
# https://www.hackerrank.com/domains/tutorials/10-days-of-statistics
# Day 4

import sys

a, b = list(map(float, sys.stdin.readline().split()))
a, b = a / (a + b), b / (a + b)

prob = 20 * (a ** 3) * (b ** 3)
prob += 15 * (a ** 4) * (b ** 2)
prob += 6 * (a ** 5) * (b ** 1)
prob += 1 * (a ** 6) * (b ** 0)
sys.stdout.write(str(round(prob, 3)) + '\n')
