import sys
sys.stdin = open('input.txt')

def bfs(graph, s, g):
    q = []
    visited = [0] * (len(graph) + 1)
    visited[s] = 1
    q.append(s)

    while q:
        s = q.pop(0)
        if s == g:
            return visited[s] - 1

        if graph[s]:
            for i in graph[s]:
                if visited[i] <= 0:
                    visited[i] = visited[s] + 1
                    q.append(i)
    return 0

T = int(input())

for tc in range(1, T+1):
    v, e = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int, input().split())
    graph = [[] for _ in range(v+1)]

    for i in node:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    print('#{}'.format(tc), bfs(graph, s, g))