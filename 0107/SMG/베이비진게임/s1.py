import sys
sys.stdin = open('input.txt')

T = int(input())

def babygin(player):
    count = [0]*10
    for card in player:
        count[card] += 1
    for c in range(10):
        if count[c] >= 3:
            return True
        elif c < 8 and count[c] and count[c+1] and count[c+2]:
            return True
    return False

for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    result = 0
    player1 = []
    player2 = []
    for i in range(12):
        if i % 2:
            player2.append(cards[i])
            if babygin(player2):
                result = 2
        else:
            player1.append((cards[i]))
            if babygin(player1):
                result = 1
        if result:
            print(f'#{tc} {result}')
            break
    else:
        print(f'#{tc} {result}')