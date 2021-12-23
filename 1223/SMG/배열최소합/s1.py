import sys
sys.stdin = open('input.txt')

T = int(input())

def search(visited, n, num_sum):
    global result, arr, N
    if n == N:
        if result > num_sum:
            result = num_sum
            return
    if num_sum > result:
        return
    for i in range(N):
        if i not in visited:
            search(visited+[i], n+1, num_sum+arr[n][i])

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 100000000000
    search([], 0, 0)
    print(f'#{tc} {result}')
