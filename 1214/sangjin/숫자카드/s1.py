import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N = int(input())
    A = sorted(input())
    counts = [0] * 10

    for i in range(N):
        counts[int(A[i])] += 1

    counts.reverse()
    print("#{} {} {}".format(test_case, 9-counts.index(max(counts)), max(counts)))

