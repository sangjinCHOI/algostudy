import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1 << 12):
        temp = []
        for j in range(12):
            if i & (1 << j):
                temp.append(lst[j])
        if len(temp) == N and sum(temp) == K:
            cnt += 1
    print(f'#{tc} {cnt}')