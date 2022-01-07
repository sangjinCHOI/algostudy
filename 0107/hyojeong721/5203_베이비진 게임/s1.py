import sys
sys.stdin = open('input.txt')
# 8 / 10 pass

def babygin(player):
    cnt_num = [0]*10
    res = 0

    # 카드 숫자 카운트 배열
    for i in range(len(player)):
        cnt_num[player[i]] += 1

    #triple 검사
    for i in range(10):
        if cnt_num[i] >= 3:
            res += 1
            cnt_num[i] -= 3
            break

    # run 검사
    for i in range(8):
        if cnt_num[i]-1 >= 0:
            if cnt_num[i+1]-1 >= 0:
                if cnt_num[i+2]-1 >= 0:
                    res += 1
                    break
    return res


T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))

    p1 = []
    p2 = []
    for i in range(0, 12, 2):
        p1.append(numbers[i])
        p2.append(numbers[i+1])
        if i >= 4:
            p1_res = babygin(p1)
            p2_res = babygin(p2)
            if p1_res > p2_res:
                print("#{} 1".format(tc))
                break
            elif p1_res < p2_res:
                print("#{} 2".format(tc))
                break
            elif i == 10:
                print("#{} 0".format(tc))



