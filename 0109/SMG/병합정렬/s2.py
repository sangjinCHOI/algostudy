import sys
sys.stdin = open('input.txt')

T = int(input())

def merge_sort(arr):
    global cnt
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])

    result = []
    l = r = 0
    if L[-1] > R[-1]:
        cnt += 1
    while l < len(L) and r < len(R):
        if L[l] < R[r]:
            result.append(L[l])
            l += 1
        else:
            result.append(R[r])
            r += 1
    result += L[l:]
    result += R[r:]

    return result


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    print(f'#{tc} {merge_sort(arr)[N//2]} {cnt}')