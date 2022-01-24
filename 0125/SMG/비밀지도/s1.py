def solution(n, arr1, arr2):
    answer = []
    binary1 = []
    binary2 = []
    result = [[0]*n for _ in range(n)]
    for i in arr1:
        temp = bin(i)[2:]
        if len(temp) == n:
            binary1.append(bin(i)[2:])
        else:
            while len(temp) < n:
                temp = '0' + temp
            binary1.append(temp)
    for i in arr2:
        temp = bin(i)[2:]
        if len(temp) == n:
            binary2.append(bin(i)[2:])
        else:
            while len(temp) < n:
                temp = '0' + temp
            binary2.append(temp)
    for i in range(n):
        for j in range(n):
            if binary2[i][j] == '1' or binary1[i][j] == '1':
                result[i][j] = 1
    for i in result:
        temp = ''
        for j in i:
            if j == 1:
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))