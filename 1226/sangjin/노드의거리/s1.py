import sys
sys.stdin = open('input.txt')

def bfs(S, G):
    queue = [S]

    while queue:
        S = queue.pop(0)

        if S == G:
            return dist[G]

        for E in range(1, V+1):
            if edge[S][E] == 1 and dist[E] == 0:
                queue.append(E)
                dist[E] = dist[S] + 1
    return 0


for test_case in range(1, int(input())+1):
    V, E = map(int, input().split())
    edge = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        edge[v1][v2] = 1
        edge[v2][v1] = 1
    S, G = map(int, input().split())
    dist = [0 for _ in range(V + 1)]

    print("#{} {}".format(test_case, bfs(S, G)))