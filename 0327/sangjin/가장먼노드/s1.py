def bfs(v, visited, arr):
    count = 1
    q = [[v, count]]
    while q:
        value = q.pop(0)
        v = value[0]
        count = value[1]
        if visited[v] == 0:
            visited[v] = count
            count += 1
            for e in arr[v]:
                q.append([e, count])

def solution(n, edge):
    answer = 0
    visited = [0] * (n+1)
    arr = [[] for _ in range(n+1)]
    for e in edge:
        arr[e[0]].append(e[1])
        arr[e[1]].append(e[0])

    bfs(1, visited, arr)

    for v in visited:
        if v == max(visited):
            answer += 1
    return answer