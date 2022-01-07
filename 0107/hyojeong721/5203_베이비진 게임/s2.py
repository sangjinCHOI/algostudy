import sys
sys.stdin = open('input.txt')


def babygin(player):
    cnt_num = [0]*10
    res = 0

    # 카드 숫자 카운트 배열
    for i in range(len(player)):
        cnt_num[player[i]] += 1

    #triplet 검사
    for i in range(10):
        if cnt_num[i] >= 3:
            res += 1
            cnt_num[i] -= 3
            break

    # run 검사
    for i in range(8):
        if cnt_num[i] and cnt_num[i+1] and cnt_num[i+2]:
            res += 1
            break

    return res

T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    p1 = numbers[0::2]
    p2 = numbers[1::2]

    for i in range(7):
        if i > 2:
            temp_p1 = p1[:i]
            temp_p2 = p2[:i]
            # 순서 주의! 1번 선수꺼 먼저 검사 다하고 2번 선수 카드 뽑아야함.
            p1_res = babygin(temp_p1)
            if p1_res > 0:
                print("#{} 1".format(tc))
                break

            p2_res = babygin(temp_p2)
            if 0 < p2_res:
                print("#{} 2".format(tc))
                break

            elif i == 6:
                print("#{} 0".format(tc))




