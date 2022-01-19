def solution(id_list, report, k):
    answer = [0] * len(id_list)
    #신고당한 횟수
    caution = [0] * len(id_list)

    temp_report = list(set(report))

    for people in temp_report:
        user1, user2 = people.split()
        idx = id_list.index(user2)
        caution[idx] += 1

    # k번 이상 신고당한 사람
    res_peopel = []
    for i in range(len(id_list)):
        if caution[i] >= k:
            res_peopel.append(id_list[i])

    # email 받는 횟수 저장
    for people in report:
        user1, user2 = people.split()
        if user2 in res_peopel:
            idx = id_list.index(user1)
            answer[idx] += 1
    return answer

# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2


id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
print(solution(id_list, report, k))