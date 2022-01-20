import sys
from collections import deque
sys.stdin = open('input.txt')

def calculate():
    while q:
        num, cnt = q.popleft()

        if num == M:
            return cnt

        for number in (num+1, num-1, num*2, num-10):
            if 0 < number <= 1000000 and visited[number] == 0:
                q.append((number, cnt + 1))
                visited[number] = 1

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    q = deque()
    q.append((N, 0))
    print("#{} {}".format(test_case, calculate()))