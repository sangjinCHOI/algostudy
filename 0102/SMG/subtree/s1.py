import sys
sys.stdin = open('input.txt')

T = int(input())
# 전위순회
def pre_order(n):
    global cnt
    if n:
        cnt += 1
        pre_order(L[n])
        pre_order(R[n])

for tc in range(1, T+1):
    E, N = map(int, input().split())
    edge = list(map(int, input().split()))
    L = [0]*(E+2)
    R = [0]*(E+2)
    cnt = 0
    for i in range(E):
        p, c = edge[i*2], edge[i*2+1]
        if L[p]:
            R[p] = c
        else:
            L[p] = c
    pre_order(N)
    print(f'#{tc} {cnt}')