from itertools import combinations

def solution(orders, course):
    N = len(orders)
    answer = []
    answer2 = []
    for num in course:
        result = 1
        temp = set()
        for order in range(N):
            for i in list(combinations(orders[order], num)):
                i = list(i)
                i.sort()
                i = "".join(i)
                cnt = 0
                for j in range(N):
                    if order != j:
                        check = True
                        for menu in i:
                            if menu not in orders[j]:
                                check = False
                        if check:
                            cnt += 1
                if result < cnt:
                    result = cnt
                    temp = set()
                    temp.add(i)
                elif result == cnt:
                    temp.add(i)
        answer.append(temp)

    for i in answer:
        for j in i:
            answer2.append(j)
    answer2.sort()

    return answer2

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))