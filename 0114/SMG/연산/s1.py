import sys
sys.stdin = open('input.txt')

T = int(input())

def search(n, num):
    global result, M
    if num < 0 or n > 1000000 or n > result:
        return
    if num == M:
        if n < result:
            result = n
            return
    search(n+1, num+1)
    search(n+1, num-1)
    search(n+1, num*2)
    search(n+1, num-10)
    return

for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = 1000000000
    search(0, N)
    print(f'#{tc} {result}')
