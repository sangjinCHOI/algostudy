from itertools import combinations

def solution(orders, course):
    answer = []
    for c in course:
        combi_list = []
        for order in orders:
            for combi in combinations(order, c):
                combi_list.append(''.join(sorted(combi)))
        # print(combi_list)
        order_count = {}
        for menu in combi_list:
            if menu not in order_count:
                order_count[menu] = combi_list.count(menu)
        print(order_count)
        sorted_order_count = sorted(order_count.items(), key=lambda item: item[1], reverse=True)
        # print('정렬된',sorted_order_count)

        for i in range(len(sorted_order_count)):
            max = sorted_order_count[i][1]
            if max != 1:
                answer.append(sorted_order_count[i][0])
            if i+1 < len(sorted_order_count) and sorted_order_count[i+1][1] < max:
                break

        answer.sort()
    return answer


orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course))