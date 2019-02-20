# Hackerrank 10 Days of Statistics Challenge
# https://www.hackerrank.com/domains/tutorials/10-days-of-statistics
# Day 1

def median(arr):
    if len(arr) % 2:
        return arr[len(arr)//2]
    else:
        median_sum = (arr[len(arr)//2-1] + arr[len(arr)//2])
        return median_sum // 2 if not median_sum % 2 else round(median_sum / 2, 1)

N = int(input().rstrip())
arr = sorted(list(map(int, input().split())))
n = len(arr)

arr_X = arr
arr_L = arr[:(n//2)]
arr_U = arr[(n//2)+1:] if n % 2 else arr[(n//2):]

print(median(arr_L))
print(median(arr_X))
print(median(arr_U))
