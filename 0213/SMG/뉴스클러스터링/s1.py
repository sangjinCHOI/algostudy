def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    str1_lst = []
    str2_lst = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            temp = str1[i] + str1[i+1]
            str1_lst.append(temp)
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            temp = str2[i] + str2[i+1]
            str2_lst.append(temp)

    cross = []
    for i in range(len(str1_lst)):
        for j in str2_lst:
            if str1_lst[i] == j:
                cross.append(str1_lst[i])
                str2_lst.remove(j)
                break

    plus = str1_lst + str2_lst

    if len(plus):
        answer = int(len(cross)/len(plus)*65536)
    else:
        answer = 65536


    return answer

print(solution('aa1+aa2', '	AAAA12'))