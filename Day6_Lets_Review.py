# Hackerrank 30 Days of code Challenge
# https://www.hackerrank.com/domains/tutorials/30-days-of-code
# Day 6

import sys

N = int(sys.stdin.readline())
for _ in range(N):
    string = sys.stdin.readline().rstrip()
    even = [string[idx] for idx in range(len(string)) if not idx % 2]
    odd = [string[idx]for idx in range(len(string)) if idx % 2]
    sys.stdout.write("".join(even) + ' ' + "".join(odd) + '\n')
