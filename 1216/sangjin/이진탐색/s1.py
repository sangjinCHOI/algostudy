import sys
sys.stdin = open('input.txt')

def binarysearch(page, target):
    left =  1
    right = page
    count = 0

    while left <= right:
        count += 1
        center = int((left + right) / 2)
        if center == target:
            break
        elif center > target:
            right = center
        else:
            left = center
    return count

for test_case in range(1, int(input())+1):
    P, Pa, Pb = map(int, input().split())

    if binarysearch(P, Pa) < binarysearch(P, Pb):
        result = 'A'
    elif binarysearch(P, Pa) > binarysearch(P, Pb):
        result = 'B'
    else:
        result = 0

    print("#{} {}".format(test_case, result))