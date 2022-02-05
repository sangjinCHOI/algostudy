
def solution(n, computers):
    p = [i for i in range(n)]

    def find(x):
        if x != p[x]:
            p[x] = find(p[x])
        return p[x]

    def union(a, b):
        papa = find(a)
        for i in range(n):
            if i != b and p[i] == p[b]:
                p[i] = papa
        p[b] = papa

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                union(i, j)
    print(p)
    answer = len(set(p))
    return answer


print(solution(5, [[1,1,0,1,0], [1,1,1,0,0], [0,1,1,0,0],[1,0,0,1,1], [0,0,0,1,1]]))