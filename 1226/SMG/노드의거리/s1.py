import sys
sys.stdin = open('input.txt')

T = int(input())

def bfs(S):
    global graph, visited, q
    q = [S]
    while q:
        s = q.pop(0)
        if visited[s[0]] == 0:
            visited[s[0]] = s[1] + 1
            for w in range(V+1):
                if graph[s[0]][w] == 1 and visited[w] == 0:
                    q.append((w, s[1] + 1))


for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        node = list(map(int, input().split()))
        graph[node[0]][node[1]] = 1
        graph[node[1]][node[0]] = 1
    S, G = map(int, input().split())
    visited = [0]*(V+1)
    bfs((S, -1))
    print(f'#{tc} {visited[G]}')
