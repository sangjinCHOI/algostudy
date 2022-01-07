import sys
sys.stdin = open('input.txt')

def mergesort(L):
    global cnt
    N = len(L)
    result = []

    if N > 2:
        L1 = L[0:N//2]
        L2 = L[N//2:N]
        L1 = mergesort(L1)
        L2 = mergesort(L2)

        if L1[-1] > L2[-1]:
            cnt += 1
        while L1 and L2:
            if L1[0] <= L2[0]:
                result.append(L1.pop(0))
            else:
                result.append(L2.pop(0))
        if L1:
            result.extend(L1)
        elif L2:
            result.extend(L2)

        return result

    elif N == 2:
        if L[0] > L[1]:
            cnt += 1
            result = [L[1], L[0]]
        else:
            result = [L[0], L[1]]
        return result
    elif N == 1:
        result = L
        return result


for test_case in range(1, int(input())+1):
    N = int(input())
    a = list(map(int, input().split()))
    cnt = 0

    print("#{} {} {}".format(test_case, mergesort(a)[N//2], cnt))