# Hackerrank 10 Days of Statistics Challenge
# https://www.hackerrank.com/domains/tutorials/10-days-of-statistics
# Day 7

N = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

sorted_X = sorted(X)
sorted_Y = sorted(Y)

X_rank = [(i, sorted_X.index(i)+1) for i in X]
Y_rank = [(i, sorted_Y.index(i)+1) for i in Y]

d_square = [(i[1] - j[1]) ** 2 for i, j in zip(X_rank, Y_rank)]

result = 1 - (6 * sum(d_square) / (N * (N ** 2 - 1)))

print(round(result, 3))
