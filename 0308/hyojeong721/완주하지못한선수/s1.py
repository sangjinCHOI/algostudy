def solution(participant, completion):
    par_dic = {}
    for par in participant:
        if par in par_dic:
            par_dic[par] += 1
        else:
            par_dic[par] = 1

    for com in completion:
        if com in par_dic and par_dic[com] > 1:
            par_dic[com] -= 1
        elif com in par_dic and par_dic[com] == 1:
            del par_dic[com]
    return list(par_dic.keys())[0]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))