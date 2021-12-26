import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(v):
    global visited, mat, stack
    stack = [v]
    while stack:
        v = stack.pop()
        if visited[v] == 0:
            visited[v] = 1
            for w in range(1, V+1):
                if mat[v][w] == 1 and visited[w] == 0:
                    stack.append(w)




for tc in range(1, T+1):
    V, E = map(int, input().split())
    mat = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        N, M = map(int, input().split())
        mat[N][M] +=1
    S, G = map(int, input().split())
    visited = [0]*(V+1)
    dfs(S)
    if visited[G]:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')
