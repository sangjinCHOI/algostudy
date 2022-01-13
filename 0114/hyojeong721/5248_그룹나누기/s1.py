import sys
sys.stdin = open('input.txt')


def find_set(n):
    global R
    if R[n] == n:
        return n
    else:
        return find_set(R[n])

def union(x, y):
    R[find_set(y)] = find_set(x)
    # 이부분왜 안돼?!!!

    for idx, r in enumerate(R):
        if y == r:
            R[idx] = find_set(y)




T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    R = [0] + [i for i in range(1, N+1)]

    for i in range(M):
        one = arr[i*2]
        two = arr[i*2+1]
        union(one, two)

    R = set(R)
    print("#{} {}".format(tc, len(R)-1))

