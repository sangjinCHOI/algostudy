def solution(n, edge):
    answer = 0
    graph = {}
    for i in range(1, n + 1):
        graph[i] = [i]
    for ed in edge:
        graph[ed[0]].append(ed[1])
        graph[ed[1]].append(ed[0])

    for num in range(1, n + 1):
        temp_answer = 1
        if 1 in graph[num]:
            temp_answer = 1
            answer = max(answer, temp_answer)
        else:
            for temp in graph[num]:


    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))