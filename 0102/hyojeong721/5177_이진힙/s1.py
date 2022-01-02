import sys
sys.stdin = open('input.txt')


def ancestor_sum(n):
    global res
    ancestor_idx = n//2
    res += tree[ancestor_idx]
    if ancestor_idx == 1:
        return
    ancestor_sum(ancestor_idx)


def test_tree(idx):

    while idx > 1:
        if tree[idx//2] > tree[idx]:
            tree[idx//2], tree[idx] = tree[idx], tree[idx//2]
        idx = idx // 2


def make_tree(n):
    global idx
    tree.append(n)
    if idx > 1:
        test_tree(idx)
    idx += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    idx = 1
    tree =[0]

    # tree 만들기
    for num in arr:
        make_tree(num)

    # 조상노드의 정수값 더하기
    res = 0
    ancestor_sum(N)

    print("#{} {}".format(tc, res))
