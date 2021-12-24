# import sys
# sys.stdin = open('input.txt')
#
# for test_case in range(1, int(input())+1):
#     N = int(input())
#     cards = list(map(int, input().split()))
#     winners = list(range(N))
#     tmp = []
#
#
#     while len(winners) > 1:
#         if len(winners) % 2:
#             cards.append(cards[-1])
#             winners.append(winners[-1]+1)
#         for i in range(0, len(winners)-1, 2):
#             if ((cards[winners[i]] == 1 and cards[winners[i+1]] == 2) or
#                 (cards[winners[i]] == 2 and cards[winners[i+1]] == 3) or
#                 (cards[winners[i]] == 3 and cards[winners[i+1]] == 1)):
#                 tmp.append(winners[i+1])
#             else:
#                 tmp.append(winners[i])
#         winners = tmp
#         tmp = []
#     winner = winners[0] + 1
#
#     print("#{} {}".format(test_case, winner))