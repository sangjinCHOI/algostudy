import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        idx, value = map(int, input().split())
        arr.insert(idx, value)

    result = arr[L]

    print("#{} {}".format(test_case, result))