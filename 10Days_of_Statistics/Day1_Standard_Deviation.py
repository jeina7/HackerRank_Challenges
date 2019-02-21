# Hackerrank 10 Days of Statistics Challenge
# https://www.hackerrank.com/domains/tutorials/10-days-of-statistics
# Day 1

N = int(input().rstrip())
arr = list(map(int, input().split()))

mean = sum(arr) / len(arr)
tmp = [(i - mean) ** 2 for i in arr]
print(round((sum(tmp) / len(arr)) ** 0.5, 1))
