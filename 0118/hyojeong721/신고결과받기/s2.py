# pass~!!!
def solution(id_list, report, k):
    user = {}
    caution = {}
    for i in range(len(id_list)):
        caution[id_list[i]] = 0
        user[id_list[i]] = 0

    # 한명이 동일한사람 신고하는거 제외하기
    temp = set(report)

    for case in temp:
        user1, user2 = case.split()
        caution[user2] += 1

    for person in temp:
        user1, user2 = person.split()
        if caution[user2] >= k:
            user[user1] += 1

    answer = list(user.values())
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))