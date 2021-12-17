import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    for i in range(0, N, 2):
        max_idx = i
        min_idx = i+1
        for j in range(i, N):
            if num_lst[max_idx] < num_lst[j]:
                max_idx = j
        num_lst[i], num_lst[max_idx] = num_lst[max_idx], num_lst[i]

        for j in range(i+1, N):
            if num_lst[min_idx] > num_lst[j]:
                min_idx = j
        num_lst[i+1], num_lst[min_idx] = num_lst[min_idx], num_lst[i+1]
    print(f'#{tc}', end=" ")
    for i in range(10):
        print(num_lst[i], end=" ")
    print()