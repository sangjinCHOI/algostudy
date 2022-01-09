import sys
sys.stdin = open('input.txt')

T = int(input())

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    p = arr[len(arr) // 2]
    L = []
    E = []
    R = []
    for num in arr:
        if num < p:
            L.append(num)
        elif num > p:
            R.append(num)
        else:
            E.append(num)
    return quickSort(L) + E + quickSort(R)

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {quickSort(arr)[N//2]}')