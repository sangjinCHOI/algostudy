def solution(N, stages):
    fail = []
    M = len(stages)
    for i in range(1, N + 1):
        if M:
            fail.append(stages.count(i) / M)
        else:
            fail.append(0)
        M -= stages.count(i)

    results = []
    for idx, value in enumerate(fail):
        results.append([idx + 1, value])
    results.sort(key=lambda x: x[1], reverse=True)

    answer = []
    for result in results:
        answer.append(result[0])
    return answer