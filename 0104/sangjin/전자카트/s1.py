import sys
sys.stdin = open('input.txt')

def route(x, tmp):
    global result
    visited[x] = 1

    if sum(visited) == N:
        tmp += consume[x][0]
        if result > tmp:
            result = tmp
            return
    if tmp > result:
        return

    for i in range(1, N):
        if not visited[i]:
            route(i, tmp+consume[x][i])
            visited[i] = 0

for test_case in range(1, int(input())+1):
    N = int(input())
    consume = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 99999999999999

    route(0, 0)
    print("#{} {}".format(test_case, result))
