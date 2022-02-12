def make(str):
    res = []

    for i in range(len(str) - 1):
        temp = str[i] + str[i + 1]
        if temp.isalpha():
            temp = temp.lower()
            res.append(temp)
    return res

def solution(str1, str2):
    lst1 = make(str1)
    lst2 = make(str2)

    # 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의
    if len(lst1) == 0 and len(lst2) == 0:
        return 65536

    if len(lst1) < len(lst2):
        big = lst2
        small = lst1
    else:
        big = lst1
        small = lst2

    same = 0
    for i in range(len(small)):
        if small[i] in big:
            big.remove(small[i])
            same += 1

    total = len(small) + len(big)
    answer = int(same/total * 65536)

    return answer

str1 = 'FRANCE'
str2 = 'french'

# str1='handshake'
# str2='shake hands'
solution(str1, str2)