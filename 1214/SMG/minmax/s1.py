import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    num_max = 0
    num_min = 1000000
    for i in num_lst:
        if num_max < i:
            num_max = i
        if num_min > i:
            num_min = i
    print(f'#{tc} {num_max - num_min}')
