# Hackerrank 10 Days of Statistics Challenge
# https://www.hackerrank.com/domains/tutorials/10-days-of-statistics
# Day 0

n = int(input().rstrip())
array = sorted(list(map(int, input().split())))

mean = round(sum(array) / len(array), 2)

if len(array) % 2:
    mid = len(array) // 2
    median = array[mid-1]
else:
    mid = len(array) // 2
    median = round((array[mid-1] + array[mid]) / 2, 2)

counter = dict()
for i in array:
    try:
        counter[i]
        counter[i] += 1
    except:
        counter[i] = 1
max_count = max(counter.values())
for key, value in counter.items():
    if value == max_count:
        mode = key
        break

print(mean)
print(median)
print(mode)
