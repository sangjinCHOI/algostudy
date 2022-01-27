def solution(record):
    answer = []
    user = {}
    all_code = []
    all_user_id = []
    for cord in record:
        # 일단 나눠
        if cord[0] == 'L':
            code, user_id = cord.split()
        else:
            code, user_id, nickname = cord.split()
            # 닉네임 저장해
            user[user_id] = nickname
        all_code.append(code)
        all_user_id.append(user_id)

    # 코드 해석해
    for i in range(len(all_code)):
        now_user = user[all_user_id[i]]
        if all_code[i] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(now_user))

        elif all_code[i] == "Leave":
            answer.append("{}님이 나갔습니다.".format(now_user))

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
