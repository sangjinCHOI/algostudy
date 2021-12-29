import sys
sys.stdin = open('input.txt')


def dfs(row):
    global visited, min_num, partial_num
    if partial_num > min_num:
        return

    if row == n:
        if partial_num < min_num:
            min_num = partial_num
            return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            partial_num += arr[row][i]
            dfs(row+1)
            visited[i] = 0
            partial_num -= arr[row][i]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    min_num = 9999
    partial_num = 0

    dfs(0)
    print('#{} {}'.format(tc, min_num))