def solution(n, arr1, arr2):
    arr1_binary = []
    arr2_binary = []

    for x, y in zip(arr1, arr2):
        tmp1, tmp2 = [], []
        binary1, binary2 = bin(x)[2:], bin(y)[2:]
        for _ in range(n - len(binary1)):
            tmp1.append(0)
        for _ in range(n - len(binary2)):
            tmp2.append(0)
        for a in binary1:
            tmp1.append(int(a))
        for b in binary2:
            tmp2.append(int(b))
        arr1_binary.append(tmp1)
        arr2_binary.append(tmp2)

    answer = []
    for i in range(n):
        tmp = ''
        for j in range(n):
            if arr1_binary[i][j] | arr2_binary[i][j]:
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
    return answer