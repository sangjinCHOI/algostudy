import math
def solution(fees, records):
    answer = []
    incar = {}
    time = {}
    for re in records:
        temp = re.split(" ")
        if temp[2] == 'IN':
            incar[temp[1]] = temp[0]
        else:
            if temp[1] not in time.keys():
                time[temp[1]] = 60 * (int(temp[0][:2]) - int(incar[temp[1]][:2])) + int(temp[0][3:]) - int(incar[temp[1]][3:])
            else:
                time[temp[1]] += 60 * (int(temp[0][:2]) - int(incar[temp[1]][:2])) + int(temp[0][3:]) - int(incar[temp[1]][3:])
            del incar[temp[1]]
    if incar:
        for i in incar.keys():
            if i in time:
                time[i] += + 60*(23 - int(incar[i][:2])) + 59-int(incar[i][3:])
            else:
                time[i] = + 60*(23 - int(incar[i][:2])) + 59-int(incar[i][3:])

    time = dict(sorted(time.items()))
    for val in time.values():
        if val > fees[0]:
            res = fees[1] + math.ceil((val-fees[0]) / fees[2]) * fees[3]
        else:
            res = fees[1]
        answer.append(res)
    return answer

fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
print(solution(fees, records))

