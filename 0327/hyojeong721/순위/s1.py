def solution(n, results):
    answer = 0
    graph = [[0]*(n+1) for _ in range(n+1)]

    for res in results:
        x = res[0]
        y = res[1]
        graph[x][y] = 1
        graph[y][x] = -1

    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i].count(0) == 0:
                continue
            if graph[i][j] == 1:
                for k in range(1, n+1):
                    if graph[j][k] == 1:
                        graph[i][k] = 1
                        graph[k][i] = -1
            elif graph[i][j] == -1:
                for z in range(1, n+1):
                    if graph[j][z] == -1:
                        graph[i][z] = -1
                        graph[z][i] = 1

    for i in range(1, n+1):
        if graph[i].count(0) == 2:
            answer += 1
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	))
print(solution(4, [[1,2],[2,3],[1,4]]))
print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]]))

# 2,1,5