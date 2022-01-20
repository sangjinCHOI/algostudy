def solution(id_list, report, k):
    answer = []
    reported = {}
    reporting = {}
    for i in id_list:
        reporting[i] = []
        reported[i] = 0
    for i in report:
        temp = i.split()
        if temp[1] not in reporting[temp[0]]:
            reporting[temp[0]].append(temp[1])
            reported[temp[1]] += 1
    for i in id_list:
        temp = 0
        if reporting[i]:
            for j in reporting[i]:
                if reported[j] >= k:
                    temp += 1
        answer.append(temp)
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))