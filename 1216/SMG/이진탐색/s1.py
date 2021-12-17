import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    cntA = 0
    cntB = 0
    l = 1
    r = P
    a = (l+r)//2
    while a != A:
        cntA += 1
        if a < A:
            l = a
        else:
            r = a
        a = (l+r)//2
    l = 1
    r = P
    b = (l+r)/2
    while b != B:
        cntB += 1
        if b < B:
            l = b
        else:
            r = b
        b = (l+r)//2

    if cntA < cntB:
        print(f'#{tc} A')
    elif cntA == cntB:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} B')