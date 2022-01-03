import sys
sys.stdin = open('input.txt')

T = int(input())

# 후위순회
def post_order(n):
    if n <= N:
        post_order(n*2)
        post_order(n*2+1)
        if tree[n] == 0 and (n*2+1) <= N:
            tree[n] = tree[n*2] + tree[n*2+1]
        elif tree[n] == 0:
            tree[n] = tree[n*2]

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for i in range(M):
        a, b = map(int, input().split())
        tree[a] = b
    post_order(1)
    print(f'#{tc} {tree[L]}')
