import sys
sys.stdin = open('input.txt')

def binarysearch(l, r, arr, target):
    global  cnt, check
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            cnt += 1
            return
        elif arr[m] > target:
            if check == 1:
                return
            check = 1
            r = m - 1
        else:
            if check == 2:
                return
            check = 2
            l = m + 1
    return


for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0

    for number in B:
        check = 0
        binarysearch(0, N-1, A, number)

    print("#{} {}".format(test_case, cnt))

