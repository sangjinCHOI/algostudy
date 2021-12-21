import sys
sys.stdin = open('input.txt')

def sequence(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return sequence(n-1) + (2*sequence(n-2))

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    res = sequence(n//10)
    print('#{} {}'.format(tc, res))

