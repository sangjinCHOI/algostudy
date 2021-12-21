import sys
sys.stdin = open('input.txt')

def dfs(s):
    visited[s] = 1
    for i in graph[s]:
        if visited[i] == 0:
            dfs(i)

T = int(input())
for tc in range(1, T+1):
    # v : 노드 수 / e : 간선 수
    v, e = map(int, input().split())
    # 그래프
    graph = [[] for _ in range(v+1)]
    visited = [0 for _ in range(v+1)]

    for i in range(e):
        s, g = map(int, input().split())
        graph[s].append(g)

    # s : 출발 노드 / g : 도착 노드
    s, g = map(int, input().split())
    dfs(s)
    res = 1
    if visited[g] == 0:
        res = 0

    print('#{} {}'.format(tc, res))



