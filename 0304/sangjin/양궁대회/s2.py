from itertools import combinations_with_replacement


def solution(n, info):
    answer = [0 for _ in range(11)]
    score = 0
    win = 0
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for p in combinations_with_replacement(num, n):
        ryan = [0 for _ in range(11)]
        for tmp in p:
            ryan[10 - tmp] += 1
        ryan_score, apeach_score = 0, 0

        for i, (r, a) in enumerate(zip(ryan, info)):
            if r == a == 0:
                continue
            if a >= r:
                apeach_score += (10 - i)
            elif r > a:
                ryan_score += (10 - i)

        if ryan_score > apeach_score:
            win = 1
            if (ryan_score - apeach_score) > score:
                score = ryan_score - apeach_score
                answer = ryan
    if not win:
        return [-1]
    return answer