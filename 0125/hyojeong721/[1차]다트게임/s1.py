def solution(dartResult):
    numbers = ['0', '1', '2', '3', '4','5', '6', '7', '8', '9', '10']
    #숫자 나누기
    temp = []
    i = 0
    while i < len(dartResult):
        if dartResult[i] in numbers:
            # 옵션 있는 경우
            if i+2 < len(dartResult) and dartResult[i+2] not in numbers:
                temp.append(dartResult[i:i+3])
                i += 3
            else:
                temp.append(dartResult[i:i+2])
                i += 2

    print(temp)
    temp_num = []

    for i in range(3):
        strnum = temp[i]
        num = ''
        for c in strnum:
            if c in numbers:
                num += c
            elif c in ('S', 'D', 'T'):
                break

        if 'S' in strnum:
            number = int(num)
        elif 'D' in strnum:
            number = int(num) ** 2
        elif 'T' in strnum:
            number = int(num) ** 3

        if strnum[-1] == '*':
            if temp_num:
                temp_num[-1] *= 2
            number *= 2

        elif strnum[-1] == '#':
            if '*' in temp:
                number *= (-2)
            number *= (-1)

        temp_num.append(number)


    answer = sum(temp_num)

    return answer


dartResult = '1S*2T*3S'
print(solution(dartResult))