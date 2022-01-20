from collections import deque
import sys
sys.stdin = open('input.txt')
# 이 문제에서 q를 []하면 시간초과 뜬다.

def sub_cal(N, i):
    if i == 0:
        return N + 1
    elif i == 1:
        return N - 1
    elif i == 2:
        return N * 2
    elif i == 3:
        return N - 10

def cal(N, cnt):
    q = deque()
    q.append((N, cnt))
    visited[N] = 1
    while q:
        num, cnt = q.popleft()
        for i in range(4):
            new_num = sub_cal(num, i)
            if new_num == M:
                return cnt + 1
            # deque써도 27번 조건절 없으면 시간초과 뜬다.
            if 0 < new_num <= 1000000 and visited[new_num] != 1:
                q.append((new_num, cnt+1))
                visited[new_num] = 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    print("#{} {}".format(tc, cal(N, 0)))
