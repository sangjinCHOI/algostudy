import math

def solution(progresses, speeds):
    answer = []
    res = []
    while progresses:
        pro = progresses.pop(0)
        speed = speeds.pop(0)
        com = math.ceil((100 - pro) / speed)
        res.append(com)
    test = res.pop(0)
    cnt = 0
    while res:
        cnt += 1
        temp = res.pop(0)
        if temp > test:
            answer.append(cnt)
            cnt = 0
            test = temp
    cnt += 1
    if cnt != 0:
        answer.append(cnt)

    return answer

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))