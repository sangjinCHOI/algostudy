import sys
sys.stdin = open('input.txt')
# 6/10 pass -> 세로검사에서 temp의 위치가 잘못되었다.

T = int(input())
for tc in range(1, T+1):
    # n*n 글자판 / m = 회문의 길이
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    res = 0
    # 가로 검사
    for row in arr:
        for i in range(n-m+1):
            str = row[i:i+m]
            if str == str[::-1]:
                res = str

    if res == 0:
        # 세로 검사
        for col in range(n):
            temp = ''
            for row in range(n-m+1):
                for i in range(m):
                    temp += arr[row+i][col]
                if temp == temp[::-1]:
                    res = temp

    print("#{} {}".format(tc, res))
