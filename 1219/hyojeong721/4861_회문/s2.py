import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # n*n 글자판 / m = 회문의 길이
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    res = ''
    # 가로 검사
    for row in arr:
        for i in range(n-m+1):
            string = row[i:i+m]
            if string == string[::-1]:
                res = string
    if not res:
        # 세로 검사
        for col in range(n):
            for row in range(n-m+1):
                temp = ''
                for i in range(m):
                    temp += arr[row+i][col]
                if temp == temp[::-1]:
                    res = temp

    print("#{} {}".format(tc, res))