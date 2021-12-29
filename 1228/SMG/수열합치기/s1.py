import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = list(map(int, input().split()))
    for i in range(M-1):
        nums = list(map(int, input().split()))
        for j in range(len(result)):
            if result[j] > nums[0]:
                # 새로운 사실!!
                print(nums)
                result[j:j] = nums
                print(result)
                break
        else:
            result.extend(nums)
    print(f'#{tc}', end=" ")
    for p in range(-1, -11, -1):
        print(result[p], end=" ")
    print()