def solution(tickets):
    tickets.sort(key=lambda x: x[1], reverse=True)
    routes = dict()
    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]

    stack = ["ICN"]
    answer = []
    while stack:
        depart = stack[-1]
        if depart not in routes or not routes[depart]:
            answer.append(stack.pop())
        else:
            stack.append(routes[depart].pop())
    answer.reverse()
    return answer