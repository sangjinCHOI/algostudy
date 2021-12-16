import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N = int(input())
    A = list(map(int, input().split()))

    A_lower = sorted(A)[0:len(A)//2] # 1 2 3 4 5
    A_upper = list(reversed(sorted(A)[len(A)//2:len(A)])) # 11 10 9 8 7 6

    result = []
    for idx in range(len(A_lower)):
        result.append(A_upper[idx])
        result.append(A_lower[idx])
    else:
        if len(A_lower) != len(A_upper):
            result.append(A_upper[-1])

    print("#{}".format(test_case), *result[:10])
