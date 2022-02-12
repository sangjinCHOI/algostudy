def make(str):
    res = []

    for i in range(len(str) - 1):
        temp = str[i] + str[i + 1]
        if temp.isalpha():
            temp = temp.lower()
            res.append(temp)
    return res


def solution(str1, str2):
    answer = 0
    lst1 = make(str1)
    lst2 = make(str2)

    if len(lst1) == 0 and len(lst2) == 0:
        return 65536

    if len(lst1) <= len(lst2):
        length_lst = lst1
    else:
        length_lst = lst2

    same = {}

    for i in range(len(length_lst)):
        temp = length_lst[i]
        if temp in lst2:
            same[i] = temp
            lst1[lst1.index(temp)] = 1
            lst2[lst2.index(temp)] = 1

    same_cnt = len(same)
    if same_cnt == 0:
        return 0

    while 1 in lst1:
        lst1.remove(1)
    while 1 in lst2:
        lst2.remove(1)

    sum = same_cnt + len(lst1) + len(lst2)
    if sum == 0:
        return 65536

    answer = int(same_cnt / sum * 65536)

    return