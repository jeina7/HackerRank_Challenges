# Hackerrank 30 Days of code Challenge
# https://www.hackerrank.com/domains/tutorials/30-days-of-code
# Day 25

T = int(input())

for _ in range(T):
    n = int(input())
    flag = True
    while flag:
        if n == 1:
            flag = False
        for i in range(2, int(n ** 0.5)+1):
            if n % i == 0:
                flag = False
        break
    if flag:
        print("Prime")
    else:
        print("Not prime")
