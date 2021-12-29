import sys
sys.stdin = open('input.txt')

def point(miro):
    global visited
    for i in range(n):
        for j in range(n):
            if miro[i][j] == 1:
                visited[i][j] = 1
            elif miro[i][j] == 2:
                start_idx = [i, j]
    return start_idx

def search(start_idx):
    global visited
    drow = [1, -1, 0, 0]
    dcol = [0, 0, -1, 1]

    stack = [start_idx[0], start_idx[1]]
    visited[start_idx[0]][start_idx[1]] = 1

    while stack:
        now_col = stack.pop()
        now_row = stack.pop()
        if miro[now_row][now_col] == 3:
            return 1

        for i in range(4):
            new_row = now_row + drow[i]
            new_col = now_col + dcol[i]
            if 0 <= new_row < n and 0 <= new_col < n:
                if miro[new_row][new_col] != 1:
                    if visited[new_row][new_col] != 1:
                        stack.append(new_row)
                        stack.append(new_col)
                        visited[new_row][new_col] = 1

    return 0

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    miro = [list(map(int, input())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]

    start_idx = point(miro)
    res = search((start_idx))
    print("#{} {}".format(tc, res))

