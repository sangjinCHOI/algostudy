from itertools import permutations


def solution(n, info):
    ryan = [info[i] + 1 for i in range(11)]
    answer = []
    score = 0
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in range(11):
        for p in permutations(num, i):
            ryan_score = 0
            arrow = 0
            for i in p:
                arrow += info[i] + 1
                if arrow > n:
                    break
                ryan_score += (ryan[i]) * (10 - int(i))
            if ryan_score >= score:
                answer.append(p)
    print(answer)

    #     arrow = 0
    #     for i in range(len(info)):
    #         for j in range(i, len(info))
    #             if arrow < n:
    #                 ryan[j] = info[j] + 1
    #                 arrow += info[j] + 1
    #             else:

    #                 break

    return answer
