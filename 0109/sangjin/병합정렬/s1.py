import sys
sys.stdin = open('input.txt')


def merge(L):
    N = len(L)
    if N == 1:
        return L
    else:
        L1 = merge(L[0:N // 2])
        L2 = merge(L[N // 2:N])
        return sorting(L1, L2)


def sorting(L1, L2):
    global cnt
    result = []

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


for test_case in range(1, int(input()) + 1):
    N = int(input())
    a = list(map(int, input().split()))
    cnt = 0

    print("#{} {} {}".format(test_case, merge(a)[N // 2], cnt))
