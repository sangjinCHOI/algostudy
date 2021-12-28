import sys
sys.stdin = open('input.txt')

def I(idx, num):
    numbers.insert(idx, num)

def D(idx):
    numbers.pop(idx)

def C(idx, num):
    numbers[idx] = num

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    numbers = list(map(int, input().split()))
    idx_numbers = ()

    for m in range(M):
        edit = list(input().split())
        if edit[0] == 'I':
            I(int(edit[1]), int(edit[2]))
        elif edit[0] == 'D':
            D(int(edit[1]))
        elif edit[0] == 'C':
            C(int(edit[1]), int(edit[2]))

    if L < len(numbers):
        print("#{}".format(tc), numbers[L])
    else:
        print("#{} -1".format(tc))