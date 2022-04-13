def solution(progresses, speeds):
    remain = []
    day = 0
    for i in range(len(progresses)):
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            day += 1
        remain.append(day)
        day = 0
    print(remain)

    answer = []
    stack = []

    for i in range(len(remain)):
        if len(stack) == 0:
            stack.append(remain[i])
        else:
            if stack[0] >= remain[i]:
                stack.append(remain[i])
            else:
                answer.append(len(stack))
                stack = []
                stack.append(remain[i])
    if len(stack) > 0:
        answer.append(len(stack))

    return answer