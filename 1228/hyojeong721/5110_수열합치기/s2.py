import sys
sys.stdin = open('input.txt')
def more_num(res, number):
    for i in res:
        if i > number:
            return res.index(i)
    return -1

T = int(input())
for tc in range(1, T+1):
    # 수열의 길이, 수열의 갯수
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]

    res = arr[0]
    for i in range(1, m):
        number = arr[i][0]
        idx = more_num(res, number)
        if idx != -1:
            res[idx:idx] = arr[i]
            # res = res[:idx] + arr[i] + res[idx:] -> 시간초과남
        else:
            res.extend(arr[i])

    print("#{}".format(tc), *res[::-1][:10:])