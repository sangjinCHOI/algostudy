# def solution(n, costs):
#     arr = [[0] * n for _ in range(n) ]
#     for cost in costs:
#         arr[cost[0]][cost[1]] = cost[2]
#         arr[cost[1]][cost[0]] = cost[2]
#     print(arr)
#     answer = 0
#     return answer