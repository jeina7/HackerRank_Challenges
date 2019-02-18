# Hackerrank 10 Days of Statistics Challenge
# https://www.hackerrank.com/domains/tutorials/10-days-of-statistics
# Day 1

n = int(input())
numbers = list(map(int, input().split()))
weights = list(map(int, input().split()))

weighted_sum = [i * j for i, j in zip(numbers, weights)]

print(round(sum(weighted_sum) / sum(weights), 1))
