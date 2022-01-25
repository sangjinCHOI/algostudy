def solution(n, arr1, arr2):
    answer = []
    # 이진수로 바꾸기
    for i in range(n):
        num1 = bin(arr1[i])[2:]
        num2 = bin(arr2[i])[2:]
        print(num1, num2)
        if len(num1) != n:
            arr1[i] = num1.zfill(n)
        else:
            arr1[i] = num1

        if len(num2) != n:
            arr2[i] = num2.zfill(n)
        else:
            arr2[i] = num2

    # print(arr1)
    # print(arr2)

    # 암호 해독
    for i in range(n):
        temp = ""
        for j in range(n):
            # 공백인곳
            if arr1[i][j] + arr2[i][j] == '00':
                temp += " "
            else:
                temp += "#"
        answer.append(temp)
    return answer


n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))