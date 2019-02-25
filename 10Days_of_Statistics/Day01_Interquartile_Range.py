import sys

def median(arr):
    if len(arr) % 2:
        return float(arr[len(arr)//2])
    else:
        median_sum = (arr[len(arr)//2-1] + arr[len(arr)//2])
        return round(median_sum / 2, 1)

N = int(sys.stdin.readline().rstrip())
nums = sys.stdin.readline().rstrip()
freq = sys.stdin.readline().rstrip()
nums = list(map(int, nums.split()))
freq = list(map(int, freq.split()))

arr = []
for i, j in zip(nums, freq):
    arr.extend([i for _ in range(j)])

arr = sorted(arr)
n = len(arr)
arr_L = arr[:(n//2)]
arr_U = arr[(n//2)+1:] if n % 2 else arr[(n//2):]

sys.stdout.write(str(median(arr_U) - median(arr_L)) + '\n')
