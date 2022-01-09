import sys
sys.stdin = open('input.txt')

T = int(input())


def merge(L, R):
    global cnt
    result = []
    if L[-1] > R[-1]:
        cnt += 1
    while L or R:
        if L and R:
            if L[0] <= R[0]:
                result.append(L.pop(0))
            else:
                result.append(R.pop(0))
        elif L:
            result.append(L.pop(0))
        elif R:
            result.append(R.pop(0))
    return result

def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    L = arr[:n//2]
    R = arr[n//2:]
    L = merge_sort(L)
    R = merge_sort(R)
    return merge(L, R)


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    print(f'#{tc} {merge_sort(arr)[N//2]} {cnt}')