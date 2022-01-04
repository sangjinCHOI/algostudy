# 맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면
# 이때의 합계가 얼마인지 출력하는 프로그램
import sys
sys.stdin = open('input.txt')


def search(x, y, temp):
    global res
    # 목적지에 도착했다면
    if x == N-1 and y == N-1:
        if res > temp:
            res = temp
        return

    # 목적지 도착전에 이미 합이 res보다 더 큰 경우
    if res < temp:
        return

    # 새로운 경로
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < N and ny < N:
            search(nx, ny, temp+arr[nx][ny])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 10 * (N-1) + 10 * N

    dx = [0, 1]
    dy = [1, 0]
    search(0, 0, arr[0][0])

    print("#{} {}".format(tc, res))