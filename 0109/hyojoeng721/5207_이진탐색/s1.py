import sys
sys.stdin = open('input.txt')
# 이때 B에 속한 어떤 수가 A에 들어있으면서,
# 동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수를 알아보려고 한다.

def search(num, pos):
    global cnt

    if num not in A:
        return

    l = 0
    r = n-1

    while l <= r:
        m = (l+r) // 2

        if num == A[m]:
            cnt += 1
            return
        if num < A[m]:
            if pos == -1:
                return
            r = m-1
            pos = -1
        elif num > A[m]:
            if pos == 1:
                return
            l = m+1
            pos = 1


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))

    # A 정렬안되면 pass 안됌
    A.sort()

    B = list(map(int, input().split()))
    cnt = 0

    for num in B:
        search(num, 0)

    print("#{} {}".format(tc, cnt))