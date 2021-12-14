import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N = int(input())
    A = list(map(int, input().split()))

    print("#{} {}".format(test_case, max(A)-min(A)))