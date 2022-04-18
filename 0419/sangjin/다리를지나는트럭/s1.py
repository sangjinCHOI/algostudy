def solution(bridge_length, weight, truck_weights):
    on_bridge = []
    on_time = []
    second = 0
    count = 0

    second += 1
    x = truck_weights.pop(0)
    on_bridge.append(x)
    on_time.append(second)

    while on_bridge != []:
        second += 1
        if on_time[0] + bridge_length == second:
            on_bridge.pop(0)
            on_time.pop(0)

        if truck_weights != []:
            x = truck_weights[0]
            if sum(on_bridge) + x <= weight:
                truck_weights.pop(0)
                on_bridge.append(x)
                on_time.append(second)
        else:
            continue

    answer = second
    return answer