def solution(msg):
    answer = []
    dic = {}
    dic_num = 27
    s = 0
    e = 1
    k = len(msg)
    while s < len(msg):
        temp = msg[s:e]

        if e == len(msg)+1:
            answer.append(temp_num)
            break

        if len(temp) != 1:
            if temp in dic:
                temp_num = dic[temp]
                e += 1
            else:
                dic[temp] = dic_num
                dic_num += 1
                s = e-1
                answer.append(temp_num)
        else:
            temp_num = ord(temp) - 64
            e += 1
    return answer

msg = "TOBEORNOTTOBEORTOBEORNOT"
print(solution(msg))