def per():
    global res, N

    if len(res) == N:
        print(res)
        return
    for i in range(len(numbers)):
        if visited[numbers[i]] == 0:
            visited[numbers[i]] = 1
            res.append(numbers[i])
            per()
            visited[numbers[i]] = 0
            res.pop()

N = 4
res = [1]
numbers = [i for i in range(2, N+1)]
visited = [0 for _ in range(N+1)]
visited[1] = 1
print(per())
