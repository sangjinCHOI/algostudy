import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_sum = 0
    min_sum = 999999
    for i in range(n-m+1):
        temp = 0
        for j in range(m):
            temp += numbers[i+j]
        if max_sum < temp:
            max_sum = temp
        if min_sum > temp:
            min_sum = temp
    res = max_sum - min_sum
    print('#{} {}'.format(tc, res))
