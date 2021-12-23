import sys
sys.stdin = open('input.txt')

T = int(input())

def search(n, result):
    global N
    if n == N:
        return result
    if n % 2:
        return search(n+1, result*2+1)
    else:
        return search(n+1, result*2-1)

for tc in range(1, T+1):
    N = int(input()) // 10
    res = search(1, 1)
    print(f'#{tc} {res}')
