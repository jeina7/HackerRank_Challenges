# Hackerrank 30 Days of code Challenge
# https://www.hackerrank.com/domains/tutorials/30-days-of-code
# Day 19

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        result = 0
        if n == 1:
            return 1
        for i in range(1, int(n ** 0.5)+1):
            if not n % i:
                if i == (n // i):
                    result += i
                else:
                    result += i
                    result += (n // i)
        return result


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
