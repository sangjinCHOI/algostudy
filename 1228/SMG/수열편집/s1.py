import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    nums = list(input().split())
    for i in range(M):
        temp = list(input().split())
        if temp[0] == 'I':
            nums.insert(int(temp[1]), temp[2])
        elif temp[0] == 'D':
            nums.pop(int(temp[1]))
        else:
            nums.pop(int(temp[1]))
            nums.insert(int(temp[1]), temp[2])
    if len(nums) > L:
        print(f'#{tc} {nums[L]}')
    else:
        print(f'#{tc} {-1}')