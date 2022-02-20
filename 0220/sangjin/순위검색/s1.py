def solution(info, query):
    for i in range(len(info)):
        x = info.pop(0)
        info.append(list(x.split(" ")))
    for i in range(len(query)):
        x = query.pop(0).replace(" and ", " ")
        query.append(list(x.split(" ")))

    tmp, cnt = 0, 0
    answer = []

    for q in query:
        for i in info:
            for j in range(4):
                if q[j] == "-" or i[j] == q[j]:
                    tmp += 1
            if int(i[4]) >= int(q[4]):
                tmp += 1
            if tmp == 5:
                cnt += 1
            tmp = 0
        answer.append(cnt)
        cnt = 0

    return answer