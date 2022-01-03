import sys
sys.stdin = open('input.txt')


def tree(n):
    global cnt
    if n <= N:
        tree(n*2)
        idx_tree[n] = cnt
        cnt += 1
        tree(n*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    idx_tree = [0 for _ in range(N+1)]
    cnt = 1
    tree(1)
    print("#{} {} {}".format(tc, idx_tree[1], idx_tree[N//2]))