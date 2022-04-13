def solution(priorities, location):
    answer = 0
    res = []
    cnt = 0
    for idx, val in enumerate(priorities):
        res.append((idx,val))

    while cnt < len(priorities):
        cnt += 1
        temp = res.pop(0)
        num = priorities.pop(0)
        if temp[1] < max(priorities):
            res.append(temp)
            priorities.append(num)
        else:
            answer += 1

    for index, k in enumerate(res):
        if k[0] == location:
            answer += index + 1
            break
    return answer
print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
