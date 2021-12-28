import sys
sys.stdin = open('input.txt')

def route(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx in range(N) and ny in range(N):
            if maze[nx][ny] == 3:
                dist[nx][ny] = dist[x][y]
                return dist
            if maze[nx][ny] == 0:
                maze[nx][ny] = 1
                dist[nx][ny] = dist[x][y] + 1
                route(nx, ny)

for test_case in range(1, int(input())+1):
    N = int(input())
    maze = [list(map(int, ' '.join(input()).split())) for _ in range(N)]
    dist = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x, y = i, j
            if maze[i][j] == 3:
                a, b = i, j

    route(x, y)
    print("#{} {}".format(test_case, dist[a][b]))
