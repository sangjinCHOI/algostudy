import sys
sys.stdin = open('input.txt')

T = int(input())

def search(n, visited, cost):
    global result, mat, N
    if n == N:
        if cost < result:
            result = cost
        return
    if cost > result:
        return
    for i in range(N):
        if i not in visited:
            search(n+1, visited+[i], cost+mat[n-1][i])

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    result = 1000000000
    search(0, [], 0)
    print(f'#{tc} {result}')