from itertools import combinations


def solution(relations):
    row = len(relations)
    col = len(relations[0])

    candidates = [[] for i in range(col + 1)]
    for i in range(col + 1):
        candidates[i] = combinations(range(col), i) # 0~3, i

    min_key = []
    for i in range(1, col + 1):
        for cand in candidates[i]:
            not_key = 0
            s = [[] for _ in range(row)]
            for k in cand:
                for r in range(row):
                    s[r].append(relations[r][k])
            for i in s:
                # 중복체크
                if s.count(i) >= 2:
                    not_key = 1
                    break
            if not_key == 0:
                # 단일 속성
                if len(cand) == 1:
                    min_key.append(cand)
                else:
                    for r in min_key:
                        if set(r).issubset(set(cand)):
                            break
                    else:
                        min_key.append(cand)
    return len(min_key)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))