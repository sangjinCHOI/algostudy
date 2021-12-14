import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_list = []

    for i in range(N-M+1):
        tmp = 0
        for j in range(M):
            tmp += A[i+j]
        sum_list.append(tmp)

    print("#{} {}".format(test_case, max(sum_list)-min(sum_list)))
