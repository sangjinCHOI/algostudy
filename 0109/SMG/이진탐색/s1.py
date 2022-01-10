import sys
sys.stdin = open('input.txt')

T = int(input())

def binarySearch(arr, m):
    global cnt
    l = 0
    r = len(arr)-1
    L = False
    R = False
    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == m:
            if L and R:
                cnt += 1
            elif not L and not R:
                cnt += 1
            return mid
        elif arr[mid] < m:
            l = mid + 1
            L = True
        else:
            r = mid - 1
            R = True
    return
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    arr.sort()
    cnt = 0
    for i in nums:
        binarySearch(arr, i)
    print(cnt)
