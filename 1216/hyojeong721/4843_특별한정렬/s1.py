import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    ai = list(map(int, input().split()))

    res = []
    while len(res) != 10:
        max_num = max(ai)
        ai.remove(max_num)
        res.append(max_num)
        min_num = min(ai)
        ai.remove(min_num)
        res.append(min_num)

    print('#{}'.format(tc), *res)
