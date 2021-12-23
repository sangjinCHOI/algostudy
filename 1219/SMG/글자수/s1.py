import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = list(set(input()))
    M = input()
    num_lst = []
    for i in N:
        cnt = 0
        for j in M:
            if i == j:
               cnt += 1
               num_lst.append(cnt)
    print(f'#{tc} {max(num_lst)}')