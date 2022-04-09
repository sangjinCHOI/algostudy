def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x:x[2])
    res = set([costs[0][0]])

    while len(res) != n:
        for idx, cost in enumerate(costs):
            if cost[0] in res and cost[1] in res:
                continue
            if cost[0] in res or cost[1] in res:
                res.update([cost[0], cost[1]])
                answer += cost[2]
                break
    return answer




print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))