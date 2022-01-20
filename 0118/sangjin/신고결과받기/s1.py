def solution(id_list, report, k):
    users = {}
    stops = {}
    for id in id_list:
        users[id] = 0
        stops[id] = 0

    report = set(report)
    for case in report:
        u, s = case.split()
        stops[s] += 1

    for case in report:
        u, s = case.split()
        if stops[s] >= k:
            users[u] += 1

    answer = []
    for id in id_list:
        answer.append(users[id])
    return answer