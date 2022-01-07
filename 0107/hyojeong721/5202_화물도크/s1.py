import sys
sys.stdin = open('input.txt')
# 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면, 최대 몇 대의 화물차가 이용


def schedule(time):
    global time_lst, cnt
    cnt += 1
    end = time[0]
    start = time[1]

    if time_lst:
        # 시작시간이 종료시간 이전인 거 삭제
        i = 0
        while i < len(time_lst):
            if time_lst[i][1] < end:
                time_lst.pop(i)
            else:
                i += 1

        if time_lst:
            time = time_lst.pop(0)
            schedule(time)
    else:
        return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time_lst = []

    for i in range(N):
        time = list(map(int, input().split()))
        # (종료시간, 시작시간)
        time.reverse()
        time_lst.append(tuple(time))

    # 종료시간 빠른 순으로 정렬
    time_lst.sort()
    print(time_lst)

    time = time_lst.pop(0)
    cnt = 0
    schedule(time)
    print("#{} {}".format(tc, cnt))