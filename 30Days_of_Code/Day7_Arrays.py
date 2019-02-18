# Hackerrank 30 Days of code Challenge
# https://www.hackerrank.com/domains/tutorials/30-days-of-code
# Day 7

if __name__ == '__main__':
    n = int(input())
    arr = list(input().rstrip().split())
    arr = reversed(arr)
    print(" ".join(arr))
