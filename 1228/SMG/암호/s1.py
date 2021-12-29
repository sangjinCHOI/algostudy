import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    nums = list(map(int, input().split()))
    idx = 0
    for _ in range(K):
        for __ in range(M):
            if idx == (len(nums)-1):
                idx = 0
            else:
                idx += 1
        if idx == 0:
            nums.insert(len(nums), nums[-1] + nums[0])
            idx -= 1
        else:
            nums.insert(idx, nums[idx-1] + nums[idx])
    nums.reverse()
    print(f'#{tc}', end=" ")
    for i in range(10):
        if i < len(nums):
            print(nums[i], end=" ")
    print()