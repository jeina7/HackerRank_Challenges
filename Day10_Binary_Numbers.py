# Hackerrank 30 Days of code Challenge
# https://www.hackerrank.com/domains/tutorials/30-days-of-code
# Day 10

if __name__ == '__main__':
    n = int(input())
    n = bin(n)[2:]
    count = 1
    maximum = 0

    # 두 번째 element부터 for문 돌기
    for idx, num in enumerate(n[1:]):
        if num == '1':
            # enumerate를 n[1:]로 돌려서 여기서의 idx는 n에서의 진짜 idx보다 하나 작으므로
            # 직전의 element를 확인하려면 idx-1이 아닌 idx로 접근
            if n[idx] == '1':
                count += 1
            else:
                count = 1
        else:
            count = 1
        if maximum <= count:
            maximum = count

    print(maximum)
