import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N, K = map(int, input().split())
    A = list(range(1, 13))

