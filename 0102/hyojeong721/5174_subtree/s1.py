import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    #간선의 개수 E, N
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [[] for _ in range(E+2)]

    for i in range(0, len(arr), 2):
        tree[arr[i]].append(arr[i+1])

    s = []

    if tree[N]:
        for node in tree[N]:
            s.append(node)

    cnt = 1
    while s:
        cnt += 1
        temp = s.pop()
        if tree[temp]:
            for node in tree[temp]:
                s.append(node)

    print("#{} {}".format(tc, cnt))
