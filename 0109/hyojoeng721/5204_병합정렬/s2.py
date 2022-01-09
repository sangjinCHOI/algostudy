import sys
sys.stdin = open('input.txt')

def merge_sort(arr):
    global cnt
    if len(arr) <= 1:
        return arr

    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]

    left = merge_sort(left)
    right = merge_sort(right)

    i, j = 0, 0
    res = []
    while len(left) > i and len(right) > j:
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    if i < len(left):
        res.extend(left[i:])
        cnt += 1
    elif j < len(right):
        res.extend(right[j:])

    return res



T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    A = merge_sort(arr)

    #  N//2 번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수를 출력
    print("#{} {} {}".format(tc, A[n//2], cnt))