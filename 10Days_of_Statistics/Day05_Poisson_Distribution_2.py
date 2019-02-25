# Hackerrank 10 Days of Statistics Challenge
# https://www.hackerrank.com/domains/tutorials/10-days-of-statistics
# Day 5

mean_x, mean_y = list(map(float, input().split()))

mean_A = 160 + 40 * (mean_x + mean_x ** 2)
mean_B = 128 + 40 * (mean_y + mean_y ** 2)

print(round(mean_A, 3))
print(round(mean_B, 3))
