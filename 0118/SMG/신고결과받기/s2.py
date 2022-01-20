def solution(id_list, report, k):
    answer = [0] * len(id_list)
    email = {}
    caution = {}
    for i in range(len(id_list)):
        caution[id_list[i]] = 0
        email[id_list[i]] = i
    print(caution)
    print(email)
    # 한명이 동일한사람 신고하는거 제외하기
    temp = set(report)

    for case in temp:
        user1, user2 = case.split()
        caution[user2] += 1
    print(caution)
    for person in report:
        user1, user2 = person.split()
        if caution[user2] >= k:
            answer[email[user1]] += 1


    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))