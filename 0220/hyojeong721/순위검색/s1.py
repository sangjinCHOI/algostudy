# 정확성 통과 / 효율성 0점
def solution(info, query):
    answer = []
    language = {}
    position = {}
    career = {}
    food = {}
    score = {}
    main_idx = 0
    idx = 0
    for i in info:
        language[main_idx] = i.split(" ")[idx]
        position[main_idx] = i.split(" ")[idx+1]
        career[main_idx] = i.split(" ")[idx+2]
        food[main_idx] = i.split(" ")[idx+3]
        score[main_idx] = i.split(" ")[idx + 4]
        main_idx += 1
    for q in query:
        test = q.split(" and ")
        idx_lst = []
        for index in range(len(test)):
            temp = test[index]
            #언어검사
            if index == 0:
                if temp == "-":
                    idx_lst = [i for i in range(len(info))]
                    continue
                for i, values in language.items():
                    if values == temp:
                        idx_lst.append(i)

            #직군검사
            elif index == 1:
                if temp == "-":
                    continue
                if idx_lst:
                    for i in range(len(idx_lst)):
                        temp_idx = idx_lst.pop(0)
                        if position[temp_idx] == temp:
                            idx_lst.append(temp_idx)
                else:
                    break
            # 경력검사
            elif index == 2:
                if temp == "-":
                    continue
                if idx_lst:
                    for i in range(len(idx_lst)):
                        temp_idx = idx_lst.pop(0)
                        if career[temp_idx] == temp:
                            idx_lst.append(temp_idx)
                else:
                    break
            elif index == 3:
                if idx_lst:
                    last_test = temp.split(" ")
                    for lst in range(2):
                        # 푸드검사
                        if lst == 0:
                            if last_test[lst] == "-":
                                continue
                            for i in range(len(idx_lst)):
                                temp_idx = idx_lst.pop(0)
                                if food[temp_idx] == last_test[lst]:
                                    idx_lst.append(temp_idx)
                        # 점수검사
                        elif lst == 1:
                            if last_test[lst] == "-":
                                continue
                            if idx_lst:
                                for i in range(len(idx_lst)):
                                    temp_idx = idx_lst.pop(0)
                                    if int(score[temp_idx]) >= int(last_test[lst]):
                                        idx_lst.append(temp_idx)

        answer.append(len(idx_lst))

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))