import sys
sys.stdin = open('input.txt')

def charge(curr, cnt, arr):
    global result
    if curr >= N-1:
        if result > cnt:
            result = cnt
        return

    if cnt >= result:
        return

    for i in range(1, arr[curr]+1):
        charge(curr+i, cnt+1, arr)

for test_case in range(1, int(input())+1):
    M = list(map(int, input().split()))
    N = M.pop(0)
    result = 9999999999

    charge(0, 0, M)
    print("#{} {}".format(test_case, result-1))