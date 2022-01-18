import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = 1000000000
    visited = [0]*1000001
    q = deque()
    q.append((N, 0))
    while q:
        n, cnt = q.popleft()
        if n == M:
            print(f'#{tc} {cnt}')
            break
        cnt += 1
        if 0 < n+1 <= 1000000 and not visited[n+1]:
            q.append((n+1, cnt))
            visited[n+1] = 1
        if 0 < n-1 <= 1000000 and not visited[n-1]:
            q.append((n-1, cnt))
            visited[n-1] = 1
        if 0 < n*2 <= 1000000 and not visited[n*2]:
            q.append((n*2, cnt))
            visited[n*2] = 1
        if 0 < n-10 <= 1000000 and not visited[n-10]:
            q.append((n-10, cnt))
            visited[n-10] = 1
