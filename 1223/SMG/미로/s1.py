import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = [input() for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if mat[i][j] == '2':
                start = (i, j)
            elif mat[i][j] == '3':
                end = (i, j)
            elif mat[i][j] == '1':
                visited[i][j] = 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    stack = [start]
    while stack:
        v = stack.pop()
        x = v[1]
        y = v[0]
        if visited[y][x] == 0:
            visited[y][x] = 1
            for w in range(4):
                tx = x + dx[w]
                ty = y + dy[w]
                if 0 <= tx < N and 0 <= ty < N and visited[ty][tx] == 0:
                    stack.append((ty, tx))

    print(f'#{tc} {visited[end[0]][end[1]]}')

