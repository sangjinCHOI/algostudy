import sys
sys.stdin = open('input.txt')

T = int(input())

def search(n, cnt):
    global station, N, result
    if n >= N:
        if cnt < result:
            result = cnt
        return
    if cnt > result:
        return
    for i in range(n+station[n], n, -1):
        search(i, cnt+1)

for tc in range(1, T+1):
    station = list(map(int, input().split()))
    N = station[0]
    result = 10000000000
    search(1, -1)
    print(f'#{tc} {result}')