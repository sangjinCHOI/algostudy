import sys
sys.stdin = open('input.txt')

def grouping(start, end):
    if start == end:
        return start
    elif start == end - 1:
        return rsp(start, end)
    else:
        group1 = grouping(start, (start+end)//2)
        group2 = grouping((start+end)//2 + 1, end)
        return rsp(group1, group2)


def rsp(player1, player2):
    if (cards[player1] == 1 and cards[player2] == 2 or
        cards[player1] == 2 and cards[player2] == 3 or
        cards[player1] == 3 and cards[player2] == 1):
        return player2
    else:
        return player1



for test_case in range(1, int(input())+1):
    N = int(input())
    cards = list(map(int, input().split()))

    print('#{} {}'.format(test_case, grouping(0, N-1)+1))


