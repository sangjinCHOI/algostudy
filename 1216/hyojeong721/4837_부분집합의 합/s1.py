import itertools
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    a = [i for i in range(1, 13)]

    # n개의 원소를 갖는 부분집합 중 합이 k인 집합의 갯수는?
    sub = list(itertools.combinations(a, n))

    cnt = 0
    print(sub)
    for i in sub:
        sum_list = sum(i)
        if sum_list == k:
            cnt += 1

    print('#{} {}'.format(tc, cnt))