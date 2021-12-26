import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    oven = []

    # 피자 N 개를 오븐에 넣는다.
    for idx in range(N):
        x = C.pop(0)
        oven.append([x, idx+1])
    idx += 2

    # 오븐에 피자가 1개 남을 떄까지
    while len(oven) > 1:
        a = oven.pop(0)
        oven.append([a[0]//2, a[1]])
        # 치즈가 다 녹으면 오븐에서 빼고
        if oven[-1][0] == 0:
            oven.pop()
            # 더 넣어야 할 피자가 남아 있으면 오븐에 넣는다.
            if C:
                oven.append([C.pop(0), idx])
                idx += 1

    # 오븐에 남은 1개 피자의 idx
    result = oven[0][1]

    print("#{} {}".format(test_case, result))

