def solution(N, stages):
    answer = []
    a = len(stages)
    results = []
    for i in range(1, N+1):
        temp = 0
        for j in stages:
            if i == j:
                temp += 1
        if a:
            results.append((i, temp/a))
            a -= temp
        else:
            results.append((i, 0))
    results.sort(key=lambda x:x[1], reverse=True)
    print(results)
    for i in results:
        answer.append(i[0])
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))