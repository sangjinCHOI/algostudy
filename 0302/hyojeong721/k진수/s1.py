def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base) # divmod -> 몫, 나머지
    if q:
        return convert(q, base) + T[r]
    else:
        return T[r]

def prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    num = convert(n, k)
    print(num)
    ls = num.split("0")
    temp = []

    for i in ls:
        if len(i) > 0:
            temp.append(i)

    for t in temp:
        if prime(int(t)):
            answer += 1


    return answer

n = 437674
n= 110011
k = 10
print(solution(n, k))

