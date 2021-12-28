import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    idx_lst = [i for i in range(n)]
    idx = 0

    for _ in range(k):
        if idx + m == len(idx_lst):
            idx = idx+m
            add_num = numbers[idx-1] + numbers[0]
        else:
            idx = (idx + m) % len(idx_lst)
            add_num = numbers[idx-1] + numbers[idx]

        idx_lst.append(idx)
        numbers.append(add_num)

        for i in range(idx, len(idx_lst)-1):
            idx_lst.pop(idx)
            temp = numbers.pop(idx)
            i += 1
            idx_lst.append(i)
            numbers.append(temp)

    # res = numbers[::-1][:10]
    res = numbers[-1:-11:-1]
    print("#{}".format(tc), *res)
