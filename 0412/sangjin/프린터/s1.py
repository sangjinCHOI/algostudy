def solution(priorities, location):
    copy_order = []

    while len(priorities) > 0:
        i = 0
        status = 1
        for j in range(1, len(priorities)):
            if priorities[i] < priorities[j]:
                tmp = priorities.pop(0)
                priorities.append(tmp)
                status = 0
                if location == 0:
                    location = len(priorities) - 1
                else:
                    location -= 1
                break
        if status:
            x = priorities.pop(0)
            copy_order.append(x)
            print(copy_order)
            if location != 0:
                location -= 1
            else:
                location = len(copy_order)
                break

    answer = location
    return answer