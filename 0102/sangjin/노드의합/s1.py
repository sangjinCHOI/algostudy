import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        node, value = map(int, input().split())
        tree[node] = value

    for i in range(N, 0, -1):
        if tree[i] == 0:
            if i*2+1 in range(N+1):
                tree[i] = tree[i*2] + tree[i*2+1]
            else:
                tree[i] = tree[i*2]

    print("#{} {}".format(test_case, tree[L]))

