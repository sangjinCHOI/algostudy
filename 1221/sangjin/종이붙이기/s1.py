import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N = int(input())
    A = [0, 1, 3]

    for _ in range(N // 10 - 2):
        A.append(A[-1] + 2 * A[-2])
    result = A[N//10]

    print("#{} {}".format(test_case, result))