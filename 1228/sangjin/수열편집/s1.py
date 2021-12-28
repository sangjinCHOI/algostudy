import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        action = tuple(input().split())
        if action[0] == 'I':
            arr.insert(int(action[1]), int(action[2]))
        elif action[0] == 'D':
            arr.pop(int(action[1]))
        elif action[0] == 'C':
            arr[int(action[1])] = int(action[2])

    if L in range(len(arr)):
        result = arr[L]
    else:
        result = -1

    print("#{} {}".format(test_case, result))