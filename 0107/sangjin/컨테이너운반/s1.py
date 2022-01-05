import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    W = sorted(list(map(int, input().split())), reverse=True)
    T = sorted(list(map(int, input().split())), reverse=True)
    result = 0
    # print(W, T)

    i = 0
    while W and i < min(N, M):
        if W[0] <= T[i]:
            result += W[0]
            W.pop(0)
            i += 1
        else:
            W.pop(0)

    print("#{} {}".format(test_case, result))

