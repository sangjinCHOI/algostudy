import sys
sys.stdin = open('input.txt')

from pprint import pprint

T = int(input())

def search(n):
    if visited[n]:
        return 0
    visited[n] = 1
    for i in range(1, N+1):
        if graph[n][i] and not visited[i]:
            search(i)
    return 1


for tc in range(1, T+1):
    N, M = map(int, input().split())
    M_lst = list(map(int, input().split()))
    graph = [[0]*(N+1) for _ in range(N+1)]
    visited = [0]*(N+1)
    cnt = 0
    for i in range(M):
        a, b = M_lst[i*2], M_lst[i*2+1]
        graph[a][b] = 1
        graph[b][a] = 1
    pprint(graph)
    for w in range(1, N+1):
        cnt += search(w)

    print(f'#{tc} {cnt}')