from collections import deque

def testdef(index, de, temp, idx_lst, len_info):
    if temp == "-" and index > 0:
        return idx_lst

    if index == 0:
        if temp == "-":
            idx_lst = deque([i for i in range(len_info)])
            return idx_lst
        else:
            for i, values in de.items():
                if values == temp:
                    idx_lst.append(i)
    else:
        for i in range(len(idx_lst)):
            temp_idx = idx_lst.popleft()
            if de[temp_idx] == temp:
                idx_lst.append(temp_idx)
    return idx_lst

def last_test(food, score, temp, idx_lst):

    last_test = temp.split(" ")
    for lst in range(2):
        # 푸드검사
        if lst == 0:
            if last_test[lst] == "-":
                continue
            for i in range(len(idx_lst)):
                temp_idx = idx_lst.popleft()
                if food[temp_idx] == last_test[lst]:
                    idx_lst.append(temp_idx)
        # 점수검사
        elif lst == 1:
            if last_test[lst] == "-":
                continue
            if idx_lst:
                for i in range(len(idx_lst)):
                    temp_idx = idx_lst.popleft()
                    if int(score[temp_idx]) >= int(last_test[lst]):
                        idx_lst.append(temp_idx)
    return idx_lst


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
        test = tuple(q.split(" and "))
        idx_lst = deque()
        for index in range(len(test)):
            temp = test[index]
            #언어검사
            if index == 0:
                idx_lst = testdef(0, language, temp, idx_lst, len(info))

            #직군검사
            elif index == 1:
                if idx_lst:
                    idx_lst = testdef(index, position, temp, idx_lst, len(info))
                else:
                    break
            # 경력검사
            elif index == 2:
                if idx_lst:
                    idx_lst = testdef(index, career, temp, idx_lst, len(info))
                else:
                    break

            # 푸드, 점수 검사
            elif index == 3:
                if idx_lst:
                    idx_lst = last_test(food, score, temp, idx_lst)
                else:
                    break
        answer.append(len(idx_lst))
    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))