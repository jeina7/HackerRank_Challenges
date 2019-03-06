# Hackerrank 30 Days of code Challenge
# https://www.hackerrank.com/domains/tutorials/30-days-of-code
# Day 26

real_day, real_month, real_year = list(map(int, input().split()))
expc_day, expc_month, expc_year = list(map(int, input().split()))

if real_year > expc_year:
    print(10000)
elif real_year == expc_year:
    if real_month > expc_month:
        print((real_month - expc_month) * 500)
    else:
        if real_day > expc_day:
            print((real_day - expc_day) * 15)
        else:
            print(0)
else:
    print(0)
