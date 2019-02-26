# Hackerrank 10 Days of Statistics Challenge
# https://www.hackerrank.com/domains/tutorials/10-days-of-statistics
# Day 6

N = int(input())
mean = int(input())
std = int(input())
prob = float(input())
z = float(input())

mean *= N
std *= (N ** 0.5)

A = -z * std + mean
B = z * std + mean

print(round(A / N, 2))
print(round(B / N, 2))
