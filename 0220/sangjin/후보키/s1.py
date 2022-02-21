from itertools import combinations


def solution(relation):
    n = len(relation)
    m = len(relation[0])
    comb = []

    for i in range(2, m + 1):
        comb.extend(list(combinations(range(m), i)))

    cnt = 0
    tmp = []
    key = []
    for i in range(m):
        for j in range(n):
            tmp.append(relation[j][i])
        if len(tmp) == len(set(tmp)):
            key.append(i)
            cnt += 1
        tmp = []

    x = ""
    for c in comb:
        status = 1
        for k in key:
            if k in c:
                status = 0
            else:
                status = status and 1

        if status:
            for i in range(n):
                for j in range(len(c)):
                    x += relation[i][c[j]]
                tmp.append(x)
                x = ""
            if len(tmp) == len(set(tmp)):
                for w in range(len(c)):
                    key.append(c[w])
                key = list(set(key))
                cnt += 1
            tmp = []

    answer = cnt
    return answer