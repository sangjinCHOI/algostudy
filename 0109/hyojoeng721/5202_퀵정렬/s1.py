import sys
sys.stdin = open('input.txt')
# 퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고,
# A[N//2]에 저장된 값을 출력하는 프로그램을 만드시오
def quick(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst)//2]
    lst.remove(pivot)

    left, right, same = [], [], []

    for n in lst:
        if n < pivot:
            left.append(n)
        elif n > pivot:
            right.append(n)
        else:
            same.append(n)

    return quick(left) + same + [pivot] + quick(right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    A = []

    A = quick(arr)

    # N/2번 원소를 출력
    print("#{} {}".format(tc, A[N//2]))