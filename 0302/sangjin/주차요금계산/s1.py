def solution(fees, records):
    answer = []
    records = [record.split(" ") for record in records]
    garage = []
    time = []
    for record in records:
        if record[2] == "IN":
            garage.append((record[0], record[1]))
        elif record[2] == "OUT":
            for i in range(len(garage)):
                if garage[i][1] == record[1]:
                    x = garage.pop(i)
                    tmp = (int(record[0][:2]) - int(x[0][:2])) * 60 + (int(record[0][3:]) - int(x[0][3:]))
                    if time:
                        for t in range(len(time)):
                            if time[t][1] == record[1]:
                                y = time.pop(t)
                                time.append((tmp + y[0], record[1]))
                                break
                        else:
                            time.append((tmp, record[1]))
                    else:
                        time.append((tmp, record[1]))
                    break
    while garage:
        x = garage.pop()
        tmp = (23 - int(x[0][:2])) * 60 + (59 - int(x[0][3:]))
        if time:
            for t in range(len(time)):
                if time[t][1] == x[1]:
                    y = time.pop(t)
                    time.append((tmp + y[0], x[1]))
                    break
            else:
                time.append((tmp, x[1]))
        else:
            time.append((tmp, x[1]))

    for t in time:
        if t[0] <= fees[0]:
            answer.append((fees[1], t[1]))
        elif t[0] >= fees[0]:
            if (t[0] - fees[0]) % fees[2]:
                answer.append((fees[1] + ((t[0] - fees[0]) // fees[2] + 1) * fees[3], t[1]))
            else:
                answer.append((fees[1] + (t[0] - fees[0]) // fees[2] * fees[3], t[1]))

    answer = sorted(answer, key=lambda x: x[1])
    charge = [a[0] for a in answer]
    return charge