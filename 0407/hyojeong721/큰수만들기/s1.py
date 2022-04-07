

def solution(number, k):
    #문자열을 자른다.
    temp = number[:len(number)-k+1]
    index = 0
    for idx, val in enumerate(temp):
        if int(val) > int(temp[index]):
            index=idx

    if index <= k:
        str_temp = list(map(int, number[index:]))
        cnt = 0
        i = 1
        while cnt < k-index:
            if i >= len(str_temp):
                break
            if str_temp[i-1] < str_temp[i]:
                str_temp.pop(i-1)
                cnt += 1
            else:
                i += 1
    else:
        str_temp = list(map(int, number))
        for i in range(k):
            num = min(str_temp)
            str_temp.remove(num)
    answer = "".join(list(map(str, str_temp)))

    return answer

print(solution("4177252841", 4))