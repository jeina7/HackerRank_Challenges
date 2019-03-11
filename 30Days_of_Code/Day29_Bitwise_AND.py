# Hackerrank 30 Days of code Challenge
# https://www.hackerrank.com/domains/tutorials/30-days-of-code
# Day 29

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])
        k = int(nk[1])

        maximum = 0

        for i in range(1, n+1):
            for j in range(1, i):
                result = i & j
                if (result > maximum) and (result < k):
                    maximum = result
            if maximum == k-1:
                    break

        print(maximum)
