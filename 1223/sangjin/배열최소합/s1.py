import sys
from itertools import permutations
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    orders = list(permutations(range(N)))
    min_value = 999999999

    for order in orders:
        tmp = 0
        for i in range(N):
            tmp += arr[i][order[i]]

        if tmp < min_value:
            min_value = tmp

    print("#{} {}".format(test_case, min_value))
