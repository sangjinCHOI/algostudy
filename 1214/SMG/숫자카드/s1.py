import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = input()
    cnt = [0] * 10
    for i in cards:
        cnt[int(i)] += 1
    cnt_max = 0
    max_idx = 0
    for j in range(10):
        if cnt_max <= cnt[j]:
            cnt_max = cnt[j]
            max_idx = j
    print(f'#{tc} {max_idx} {cnt_max}')