# Hackerrank 30 Days of code Challenge
# https://www.hackerrank.com/domains/tutorials/30-days-of-code
# Day 17

class Calculator:
    def power(self, n, p):
        if (n >= 0) and (p >= 0):
            return n ** p
        else:
            raise Exception("n and p should be non-negative")

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)
