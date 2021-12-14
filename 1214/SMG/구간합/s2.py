import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    sum_list = []
    for i in range(N-M+1):
        sum_list.append(sum(nums[i:i+M]))

    result = max(sum_list)-min(sum_list)

    print('#{0} {1}'.format(tc, result))