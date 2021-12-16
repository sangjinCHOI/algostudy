import sys
sys.stdin = open('input.txt')

def search(page, vs):
    global p
    res = 0
    l = 1
    r = p
    while vs >= res:
        c = (l + r) // 2
        if c == page:
            break
        elif c < page:
            l = c
        else:
            r = c
        res += 1
    return res

T = int(input())
for tc in range(1, T+1):
    p, a, b = map(int, input().split())
    res_a = search(a, 99999)
    res_b = search(b, res_a)

    if res_a < res_b:
        print('#{} A'.format(tc))
    elif res_a == res_b:
        print('#{} 0'.format(tc))
    else:
        print('#{} B'.format(tc))
