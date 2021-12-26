import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = input().split()
    ans_idx = 0

    for i in range(m):
        ans_idx = (ans_idx+1) % n

    print("#{}".format(tc), arr[ans_idx])
