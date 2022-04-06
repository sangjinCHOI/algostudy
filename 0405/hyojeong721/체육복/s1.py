def solution(n, lost, reserve):
    answer = 0
    res = [1] * (n + 2)
    for i in reserve:
        res[i] += 1
    for j in lost:
        res[j] -= 1

    for i in range(1, n + 1):
        if res[i - 1] == 0 and res[i] == 2:
            res[i - 1] += 1
            res[i] -= 1
        elif res[i] == 2 and res[i + 1] == 0:
            res[i] -= 1
            res[i + 1] += 1

    answer = len(res) - res.count(0) - 2

    return answer