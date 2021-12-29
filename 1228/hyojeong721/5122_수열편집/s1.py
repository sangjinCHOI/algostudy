import sys
sys.stdin = open('input.txt')
# 런타임에러
def I(idx, num):

    for i in range(idx, len(idx_numbers)):
        if idx_numbers[i][0] >= idx:
            idx_numbers[i][0] += 1

    idx_numbers.append([idx, num])

def D(idx):
    for i in range(len(idx_numbers)):
        if idx_numbers[i][0] > idx:
            idx_numbers[i][0] -= 1
        elif idx_numbers[i][0] == idx:
            temp_idx = i

    idx_numbers.pop(temp_idx)

def C(idx, num):
    for i in range(len(idx_numbers)):
        if idx_numbers[i][0] == idx:
            idx_numbers[i][1] = num

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    number = list(map(int, input().split()))
    idx_numbers = []

    for idx in range(N):
        idx_numbers.append([idx, number[idx]])

    for m in range(M):
        edit = list(input().split())
        if edit[0] == 'I':
            I(int(edit[1]), int(edit[2]))
        elif edit[0] == 'D':
            D(int(edit[1]))
        elif edit[0] == 'C':
            C(int(edit[1]), int(edit[2]))

    for i in range(len(idx_numbers)):
        if L == idx_numbers[i][0]:
            print("#{}".format(tc), idx_numbers[i][1])
            break
    else:
        print("#{} -1".format(tc))