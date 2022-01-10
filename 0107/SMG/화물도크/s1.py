import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    truck = [tuple(map(int, input().split())) for _ in range(N)]
    truck.sort(key=lambda x: x[1])
    cnt = 0
    now = 0
    for i in truck:
        if now <= i[0]:
            now = i[1]
            cnt += 1
    print(f'#{tc} {cnt}')