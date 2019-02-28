# Hackerrank 30 Days of code Challenge
# https://www.hackerrank.com/domains/tutorials/30-days-of-code
# Day 20

def swap(array, idx1, idx2):
    array[idx1], array[idx2] = array[idx2], array[idx1]

n = int(input().strip())
a = list(map(int, input().strip().split()))

result = 0
for _ in range(n):
    count = 0
    for idx in range(n-1):
        if a[idx] > a[idx+1]:
            swap(a, idx, idx+1)
            count += 1
    if count == 0:
            break
    result += count

print("Array is sorted in {} swaps.".format(result))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))
