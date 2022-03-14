def solution(brown, yellow):
    p = brown + yellow
    answer = []

    for i in range(1, (brown + 4) // 2):
        a, b = i, (brown + 4) // 2 - i

        if a * b == brown + yellow and a >= b:
            answer.append(a)
            answer.append(b)

    return answer