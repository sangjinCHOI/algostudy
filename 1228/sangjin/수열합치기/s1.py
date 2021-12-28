import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M-1):
        tmp = list(map(int, input().split()))

        for idx in range(len(arr)):
            if arr[idx] > tmp[0]:
                arr = arr[:idx] + tmp + arr[idx:]
                if len(arr) > M + 10:
                    arr = arr[len(arr)-M-10:len(arr)]
                break
        else:
            arr += tmp

    result = arr[-1:-11:-1]
    print("#{}".format(test_case), *result)