import sys
sys.stdin = open('input.txt')

def check_run(player, card):
    if card - 1 in player and card + 1 in player:
        return True
    elif card + 1 in player and card + 2 in player:
        return True
    elif card - 1 in player and card - 2 in player:
        return True
    else:
        return False

def check_triplet(player, card):
    if player.count(card) == 3:
        return True
    else:
        return False

for test_case in range(1, int(input())+1):
    cards = list(map(int, input().split()))
    player1 = []
    player2 = []
    winner = 0

    for i in range(6):
        player1.append(cards[i * 2])
        player2.append(cards[i * 2 + 1])

        if check_run(player1, cards[i * 2]) or check_triplet(player1, cards[i * 2]):
            winner = 1
            break
        elif check_run(player2, cards[i * 2 + 1]) or check_triplet(player2, cards[i * 2 + 1]):
            winner = 2
            break

    print("#{} {}".format(test_case, winner))