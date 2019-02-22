# Hackerrank 30 Days of code Challenge
# https://www.hackerrank.com/domains/tutorials/30-days-of-code
# Day 14

class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.__elements.sort()
        self.maximumDifference = self.__elements[-1] - self.__elements[0]



_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
