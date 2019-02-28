# Hackerrank 10 Days of Statistics Challenge
# https://www.hackerrank.com/domains/tutorials/10-days-of-statistics
# Day 9

from sklearn import linear_model

m, n = list(map(int, input().split()))
xx = []
yy = []
for _ in range(n):
    data = list(map(float, input().split()))
    x, y = data[:-1], data[-1]
    xx.append(x)
    yy.append(y)

lm = linear_model.LinearRegression()
lm.fit(xx, yy)
a = lm.intercept_
b = lm.coef_

q = int(input())
xx_test = []
for _ in range(q):
    x_test = list(map(float, input().split()))
    xx_test.append(x_test)

for i in range(q):
    print(a + sum(b * xx_test[i]))
