# Hackerrank 10 Days of Statistics Challenge
# https://www.hackerrank.com/domains/tutorials/10-days-of-statistics
# Day 7

N = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

mean_X = sum(X) / len(X)
mean_Y = sum(Y) / len(Y)

tmp_X = [((i - mean_X) ** 2) for i in X]
tmp_Y = [((i - mean_Y) ** 2) for i in Y]

std_X = (sum(tmp_X) / len(tmp_X)) ** 0.5
std_Y = (sum(tmp_Y) / len(tmp_Y)) ** 0.5

X_Y = [(i - mean_X) * (j - mean_Y) for i, j in zip(X, Y)]

pearson = sum(X_Y) / (N * std_X * std_Y)

print(round(pearson, 3))
