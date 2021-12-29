import sys
sys.stdin = open('input.txt')


def game(i, j):
    a = arr[i]
    b = arr[j]

    if a == 1:
        if b == 1:
            return i
        elif b == 2:
            return j
        elif b == 3:
            return i
    elif a == 2:
        if b == 1:
            return i
        elif b == 2:
            return i
        elif b == 3:
            return j
    elif a == 3:
        if b == 1:
            return j
        elif b == 2:
            return i
        elif b == 3:
            return i


def gamer(s, e):
    if s == e:
        return s

    a = gamer(s, (s+e)//2)
    b = gamer((s+e)//2+1, e)
    res = game(a, b)

    return res

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    winner = gamer(1, n)
    print("#{} {}".format(tc, winner))