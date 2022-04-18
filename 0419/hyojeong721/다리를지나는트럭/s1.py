def solution(length, weight, truck):
    answer = 0
    size = len(truck)
    on_bridge = [0] * length
    pass_truck = []

    while len(pass_truck) < size:
        answer += 1
        top = on_bridge.pop(0)
        if top != 0:
            pass_truck.append(top)
        if truck:
            if sum(on_bridge) + truck[0] <= weight:
                on_bridge.append(truck.pop(0))
            else:
                on_bridge.append(0)

    return answer

print(solution(2, 10, 	[7,4,5,6])) #8
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])) #8

