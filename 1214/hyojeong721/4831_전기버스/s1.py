import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    k, n, m = map(int, input().split())
    charge = list(map(int, input().split()))

    cnt = 0
    now = 0

    while now + k < n:
        temp = now + k

        for i in range(k):
            if temp in charge:
                now = temp
                cnt += 1
                break
            else:
                temp -= 1
        else:
            cnt = 0
            break

    print('#{} {}'.format(tc, cnt))



