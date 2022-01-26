def solution(dartResult):
    calc = []
    idx = 0

    while idx < len(dartResult):
        # case: 10 or digit,
        if dartResult[idx] == '1' and dartResult[idx + 1] == '0':
            calc.append(10)
            idx += 1
        elif dartResult[idx].isdigit():
            calc.append(int(dartResult[idx]))
        # case: S, D, T
        elif dartResult[idx] == 'S':
            calc[-1] = pow(calc[-1], 1)
        elif dartResult[idx] == 'D':
            calc[-1] = pow(calc[-1], 2)
        elif dartResult[idx] == 'T':
            calc[-1] = pow(calc[-1], 3)
        # case: *
        elif dartResult[idx] == '*':
            if len(calc) > 1:
                calc[-2] *= 2
            calc[-1] *= 2
        # case: #
        elif dartResult[idx] == '#':
            calc[-1] *= -1
        # idx ++
        idx += 1

    answer = sum(calc)
    return answer