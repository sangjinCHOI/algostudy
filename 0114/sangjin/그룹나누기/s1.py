import sys
sys.stdin = open('input.txt')

def find(x):
    while p[x] != x:
        x = p[x]
    return x
for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    p = list(range(N+1))

    for i in range(M):
        s = numbers[2*i]
        e = numbers[2*i+1]
        p[find(e)] = find(s)

    result = 0
    for i in range(1, N+1):
        if p[i] == i:
            result += 1

    print("#{} {}".format(test_case, result))