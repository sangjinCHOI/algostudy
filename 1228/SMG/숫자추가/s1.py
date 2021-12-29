import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    nums = list(map(int, input().split()))
    for i in range(M):
        idx, num = map(int, input().split())
        nums.insert(idx, num)
    print(f'#{tc} {nums[L]}')