def solution(str1, str2):
    arr1, arr2 = [], []
    for i in range(len(str1) - 1):
        if (str1[i] + str1[i + 1]).isalpha():
            arr1.append((str1[i] + str1[i + 1]).upper())
    for i in range(len(str2) - 1):
        if (str2[i] + str2[i + 1]).isalpha():
            arr2.append((str2[i] + str2[i + 1]).upper())
    elements = list(set(arr1 + arr2))
    print(arr1, arr2)
    print(elements)

    if arr1 == [] and arr2 == []:
        answer = 65536
    else:
        a, b = 0, 0
        for e in elements:
            a += min(arr1.count(e), arr2.count(e))
            b += max(arr1.count(e), arr2.count(e))
        answer = int(a / b * 65536)

    return answer