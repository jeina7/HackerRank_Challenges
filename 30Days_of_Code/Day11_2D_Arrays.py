# Hackerrank 30 Days of code Challenge
# https://www.hackerrank.com/domains/tutorials/30-days-of-code
# Day 11

if __name__ == '__main__':
    def sum_filter(arr, row, col):
        result = 0
        result += sum(arr[row][col:col+3])
        result += arr[row+1][col+1]
        result += sum(arr[row+2][col:col+3])
        return result

    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # 리스트의 요소가 -9~9이므로 초기 maximum값은 최소값인 -9 * 7 = -63으로 설정
    maximum = -9 * 7
    for row in range(4):
        a = sum_filter(arr, row, 0)
        b = sum_filter(arr, row, 1)
        c = sum_filter(arr, row, 2)
        d = sum_filter(arr, row, 3)
        row_max = max([a, b, c, d])
        maximum = row_max if row_max > maximum else maximum

print(maximum)
