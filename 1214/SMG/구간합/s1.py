import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    v = list(map(int, input().split()))
    sum_max = 0
    sum_min = 100000000
    for i in range(N-M+1):
        temp = 0
        for j in range(M):
            temp += v[i+j]
        if sum_max < temp:
            sum_max = temp
        if sum_min > temp:
            sum_min = temp
    print(f'#{tc} {sum_max-sum_min}')