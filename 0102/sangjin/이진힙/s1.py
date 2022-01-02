import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0 for _ in range(N+1)]

    for i in range(1, N+1):
        tree[i] = arr[i-1]
        if i > 1:
            tmp = i
            while tmp > 1 and tree[tmp//2] > tree[tmp]:
                tree[tmp//2], tree[tmp] = tree[tmp], tree[tmp//2]
                tmp //= 2

    result = 0
    while N:
        N //= 2
        result += tree[N]

    print("#{} {}".format(test_case, result))
