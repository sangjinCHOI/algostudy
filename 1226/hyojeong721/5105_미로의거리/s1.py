import sys
sys.stdin = open('input.txt')

def search(miro, start_row, start_col):
    n = len(miro)
    q = [start_row, start_col]
    visited = [[0] * n for _ in range(n)]
    visited[start_row][start_col] = 1

    drow = [-1, 0, 0, 1]
    dcol = [0, -1, 1, 0]

    while q:
        now_row = q.pop(0)
        now_col = q.pop(0)

        if miro[now_row][now_col] == 3:
            return visited[now_row][now_col] - 2

        for i in range(4):
            next_row = now_row + drow[i]
            next_col = now_col + dcol[i]


            # 미로 안에 있냐?
            if 0 <= next_row < n and 0 <= next_col < n:
                # 길인가?
                if miro[next_row][next_col] != 1:
                    # 방문한 적 없냐?
                    if visited[next_row][next_col] == 0:
                        visited[next_row][next_col] = visited[now_row][now_col] + 1
                        q.append(next_row)
                        q.append(next_col)
    return 0

T = int(input())

# 0은 통로, 1은 벽, 2는 출발, 3은 도착
for tc in range(1, T+1):
    n = int(input())
    miro = [list(map(int, input())) for _ in range(n)]

    for i in range(n):
        if 2 in miro[i]:
            start_row = i
            start_col = miro[i].index(2)

    res = search(miro, start_row, start_col)


    print("#{} {}".format(tc, res))
