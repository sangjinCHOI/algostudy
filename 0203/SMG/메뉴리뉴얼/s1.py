from itertools import combinations

def solution(orders, course):
    N = len(orders)
    answer = []
    answer2 = []
    for num in course:
        result = 1
        temp = set()
        for order in range(N):
            for comb in list(combinations(orders[order], num)):
                comb = list(comb)
                comb.sort()
                comb = "".join(comb)
                cnt = 0
                for order2 in range(N):
                    if order != order2:
                        check = True
                        for menu in comb:
                            if menu not in orders[order2]:
                                check = False
                        if check:
                            cnt += 1
                if result < cnt:
                    result = cnt
                    temp = set()
                    temp.add(comb)
                elif result == cnt:
                    temp.add(comb)
        answer.append(temp)

    for i in answer:
        for j in i:
            answer2.append(j)
    answer2.sort()

    return answer2

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))