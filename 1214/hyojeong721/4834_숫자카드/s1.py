import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 카드 갯수
    arr = list(map(int, input()))

    card = [0] * 10
    # 적힌카드 숫자에 카드 갯수 추가
    for i in range(N):
        card[arr[i]] += 1

    # max_card = 가장 많은 카드 갯수
    # max_card_number = 가장 많은 카드에 적힌 숫자
    max_card = card[0]
    max_card_number = 0

    # 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력
    for i in range(10):
        if max_card <= card[i]:
            max_card_number = i
            max_card = card[i]

    print("#{} {} {}".format(tc, max_card_number, max_card))





