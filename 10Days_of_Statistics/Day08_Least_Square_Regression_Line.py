# Hackerrank 10 Days of Statistics Challenge
# https://www.hackerrank.com/domains/tutorials/10-days-of-statistics
# Day 8

scores = []
for _ in range(5):
    x, y = tuple(map(int, input().split()))
    scores.append((x, y))

n = len(scores)
x = [i[0] for i in scores]
y = [i[1] for i in scores]
xy = [i[0] * i[1] for i in scores]
x_square = [i[0] ** 2 for i in scores]
x_mean = sum([i[0] for i in scores]) / n
y_mean = sum([i[1] for i in scores]) / n

b = (n * sum(xy) - sum(x) * sum(y)) / (n * sum(x_square) - (sum(x) ** 2))
a = y_mean - b * x_mean

result = a + b * 80
print(round(result, 3))
