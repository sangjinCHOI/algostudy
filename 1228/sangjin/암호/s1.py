import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    idx = 0

    for _ in range(K):
        if idx + M < len(arr):
            idx += M
            arr.insert(idx, arr[idx-1]+arr[idx])
        elif idx + M == len(arr):
            idx = -1
            arr.append(arr[idx+1]+arr[idx])
        else:
            idx = idx + M - len(arr)
            arr.insert(idx, arr[idx - 1] + arr[idx])

    password = arr[-1:-11:-1]
    print("#{}".format(test_case), *password)


