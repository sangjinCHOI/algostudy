import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [0, 1]
dy = [1, 0]

def search(x, y, nums_sum):
    global result, mat, N
    if x == N-1 and y == N-1:
        if nums_sum < result:
            result = nums_sum
    else:
        if nums_sum > result:
            return
        else:
            for w in range(2):
                tx = x + dx[w]
                ty = y + dy[w]
                if 0 <= tx < N and 0 <= ty < N:
                    search(tx, ty, nums_sum + mat[ty][tx])

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    result = 1000000000000
    search(0, 0, mat[0][0])
    print(f'#{tc} {result}')