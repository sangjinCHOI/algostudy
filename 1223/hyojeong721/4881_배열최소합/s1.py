import sys
sys.stdin = open('input.txt')
# 3*3만 생각해서 품.. ㅠ
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    min_num = 9999

    cnt = 0
    row = 0
    col = 0

    while cnt < n*n:
        visited = [[0] * n for _ in range(n)]
        one_num = arr[row][col]
        visited[row][col] = 1
        for i in range(n):
            visited[row][i] = 1
            visited[i][col] = 1
        two = False
        for i in range(n):
            for j in range(n):
                if visited[i][j] != 1:
                    two_num = arr[i][j]
                    visited[i][j] = 1
                    for k in range(n):
                        visited[i][k] = 1
                        visited[k][j] = 1
                    two = True
                    break
                if two:
                    break
            if two:
                break

        for i in range(n):
            if 0 in visited[i]:
                idx = visited[i].index(0)
                tri_num = arr[i][idx]
                break

        if min_num > one_num + two_num + tri_num :
            min_num = one_num + two_num + tri_num

        cnt += 1
        if col < n-1:
            col += 1
        elif col == n-1:
            col = 0
            row += 1

    print("#{} {}".format(tc, min_num))