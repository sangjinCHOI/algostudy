import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    max_num = max(arr)
    min_num = min(arr)
    res = max_num - min_num
    print('#{} {}'.format(tc, res))