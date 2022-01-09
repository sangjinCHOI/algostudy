import sys
sys.stdin = open('input.txt')

def quicksort(p, s, e, arr):
    END = e
    if s > e:
        return arr
    if s == e:
        if arr[s] < arr[p]:
            arr[s], arr[p] = arr[p], arr[s]
    while s < e:
        if arr[s] <= arr[p] and arr[p] <= arr[e]:
            s += 1
            e -= 1
        # 피벗값보다 큰 S값과 큰 E값을 찾으면 바꾸기
        elif arr[s] > arr[p] and arr[e] < arr[p]:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1
        elif arr[s] <= arr[p]:
            s += 1
        elif arr[p] <= arr[e]:
            e -= 1

    if arr[s] > arr[p]:
        s -= 1
    arr[s], arr[p] = arr[p], arr[s]

    arr = quicksort(p, p+1, s-1, arr)
    arr = quicksort(s+1, s+2, END, arr)
    return arr

for test_case in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quicksort(0, 1, N-1, arr)
    # print(arr)
    print("#{} {}".format(test_case, arr[N//2]))