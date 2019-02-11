# Hackerrank 30 Days of code Challenge
# https://www.hackerrank.com/domains/tutorials/30-days-of-code
# Day 3

if __name__ == '__main__':
    N = int(input())
    if N % 2:
        print("Weird")
    else:
        if (6 <= N) and (N <= 20):
            print("Weird")
        else:
            print("Not Weird")
