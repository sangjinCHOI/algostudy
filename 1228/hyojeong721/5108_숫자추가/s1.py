import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    #  수열의 길이 N, 추가 횟수 M, 출력할 인덱스 번호 L
    n, m, l = map(int, input().split())
    arr = list(map(int, input().split()))
    add_num = [list(map(int, input().split())) for _ in range(m)]
    print(add_num)

    for i in range(m):
        idx = add_num[i][0]
        number = [add_num[i][1]]
        left = arr[:idx]
        right = arr[idx:]
        arr = left + number + right

    print('#{} {}'.format(tc, arr[l]))