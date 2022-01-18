def solution(id_list, report, k):
    n = len(report)
    # 사람당 신고당한 횟수 저장하는 caution
    # 이메일 받는 카운트 저장하는 email
    caution = dict()
    email = dict()
    for user in id_list:
        caution[user] = 0
        email[user] = 0

    rep = []
    for i in range(len(report)):
        user, caution_person = report[i].split()
        if [user, caution_person] not in rep:
            rep.append([user, caution_person])

    # 신고 횟수 기록
    res_caution = set()
    for i in range(len(rep)):
        caution[rep[i][1]] += 1
        # 기준치 넘는 id만 따로 res_id에 저장
        if caution[rep[i][1]] >= k:
            res_caution.add(rep[i][1])

    # 이메일 받을 횟수 기록
    for i in range(len(rep)):
        user = rep[i][0]
        if rep[i][1] in res_caution:
            email[user] += 1

    answer = list(email.values())
    return answer

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
print(solution(id_list, report, k))