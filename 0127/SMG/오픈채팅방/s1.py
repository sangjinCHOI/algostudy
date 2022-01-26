def solution(record):
    answer = []
    users = {}
    for i in record:
        if 'Leave' not in i:
            a, b, c = i.split()
            users[b] = c
    for i in record:
        if "Leave" in i:
            a, b = i.split()
            answer.append(f"{users[b]}님이 나갔습니다.")
        elif "Enter" in i:
            a, b, c = i.split()
            answer.append(f"{users[b]}님이 들어왔습니다.")
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))