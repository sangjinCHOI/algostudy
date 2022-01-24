def solution(numbers, hand):
    answer = ''
    node = [(1, 2), (1, 4), (2, 3), (2, 5), (3, 6), (4, 5), (4, 7), (5, 6), (5, 8), (6, 9), (7, 8), (7, 10), (8, 0), (8, 9), (9, 11), (10, 0), (0, 11)]
    graph = [[0]*13 for _ in range(13)]
    for i in node:
        graph[i[0]][i[1]] = 1
        graph[i[1]][i[0]] = 0


    return answer