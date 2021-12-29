import sys
sys.stdin = open('input.txt')
# 문제에서 더 큰 수 잘못이해한 풀이
def more_num(number):
    temp = res[:]
    temp.sort()
    print('temp',temp)
    for j in range(len(res)):
        if temp[j] > number:
            return res.index(temp[j])
    return -1

T = int(input())
for tc in range(1, T+1):
    # 수열의 길이, 수열의 갯수
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]

    res = arr[0]

    print(res)
    for i in range(1, m):
        number = arr[i][0]
        idx = more_num(number)
        print(number, idx)
        if idx != -1:
            res = res[:idx] + arr[i] + res[idx:]
        else:
            res = res + arr[i]
        print(i, res)

    print("#{}".format(tc), res[::-1][:10:])