from itertools import combinations


def solution(orders, course):
    answer = []
    for c in course:
        cases = []
        for order in orders:
            temp = combinations(sorted(order), c)
            cases += temp

        results = {}
        for case in cases:
            if case in results:
                results[case] += 1
            else:
                results[case] = 1

        for key, value in results.items():
            if value >= 2 and value == max(sorted(results.values())):
                answer.append(''.join(key))

    answer.sort()
    return answer
