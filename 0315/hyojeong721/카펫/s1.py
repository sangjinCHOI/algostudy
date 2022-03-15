def solution(brown, yellow):
    answer = [0, 1000000]

    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            x = yellow // i
            y = i
            if (x+2)*(y+2) - yellow == brown:
                if abs(answer[0] - answer[1]) > abs(x - y):
                    answer[0] = max(x, y) +2
                    answer[1] = min(x, y) +2
    return answer


brown = 14
yellow = 4
print(solution(brown, yellow))