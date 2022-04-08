def solution(routes):
    routes.sort(key=lambda x: x[1])
    cam = -30001
    answer = 0

    for route in routes:
        if cam < route[0]:
            answer += 1
            cam = route[1]

    return answer