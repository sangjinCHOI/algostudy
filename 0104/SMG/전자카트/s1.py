import sys
sys.stdin = open('input.txt')

T = int(input())

def search(now, n, visited, battery):
    global result, mat, N
    if battery > result:
        return
    if n >= N:
        battery += mat[now][0]
        if battery < result:
            result = battery
    else:
        for i in range(1, N):
            if i not in visited:
                search(i, n+1, visited+[i], battery+mat[now][i])

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    result = 1000000000
    search(0, 1, [0], 0)
    print(f'#{tc} {result}')