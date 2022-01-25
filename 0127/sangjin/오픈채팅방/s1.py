def solution(record):
    results = []
    id = {}

    for action in record:
        tmp = list(action.split())
        if len(tmp) == 3:
            id[tmp[1]] = tmp[2]

    answer = []
    for action in record:
        tmp = list(action.split())
        if tmp[0] == 'Enter':
            answer.append(id[tmp[1]] + '님이 들어왔습니다.')
        elif tmp[0] == 'Leave':
            answer.append(id[tmp[1]] + '님이 나갔습니다.')

    return answer