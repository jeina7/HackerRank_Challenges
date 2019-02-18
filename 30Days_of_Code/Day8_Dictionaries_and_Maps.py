# Hackerrank 30 Days of code Challenge
# https://www.hackerrank.com/domains/tutorials/30-days-of-code
# Day 8

import sys

N = int(sys.stdin.readline())
phonebook = dict()

for _ in range(N):
    name, number = sys.stdin.readline().rstrip().split()
    phonebook[name] = number

for _ in range(N):
    name = sys.stdin.readline().rstrip()
    # there is a testcase that the number of input names doesn't match with N
    if not name:
        break
    try:
        phonebook[name]
        print("{}={}".format(name, phonebook[name]))
    except:
        print("Not found")
