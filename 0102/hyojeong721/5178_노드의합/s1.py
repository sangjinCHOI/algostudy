import sys
sys.stdin = open('input.txt')


def make_tree(idx):
    while idx > 1:
        if idx % 2:
            tree[idx//2] = tree[idx] + tree[idx-1]
            idx -= 2
        else:
            tree[idx//2] += tree[idx]
            idx -= 1


T = int(input())
for tc in range(1, T+1):
    # N: 노드의 개수 / M: 리프노드의 개수 / L: 출력할 노드 번호
    N, M, L = map(int, input().split())
    leap_node = [list(map(int, input().split())) for _ in range(M)]
    tree = [0 for _ in range(N+1)]

    for i in range(M):
        tree[leap_node[i][0]] = leap_node[i][1]

    make_tree(N)
    print("#{} {}".format(tc, tree[L]))

