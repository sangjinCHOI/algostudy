import sys
sys.stdin = open('input.txt')

def route(x, y):
    global result
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx in range(N) and ny in range(N): # 0 <= nx, ny < N
            if maze[nx][ny] == 3:
                result = 1
                return result
            elif maze[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                route(nx, ny)


for test_case in range(1, int(input())+1):
    N = int(input())
    maze = [list(map(int, ' '.join(input()).split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x, y = i, j

    result = 0
    route(x, y)
    print("#{} {}".format(test_case, result))
