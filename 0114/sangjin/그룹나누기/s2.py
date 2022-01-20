# test case 1개 실패 : 원인 불명

import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    pairs = []
    for i in range(0, len(numbers), 2):
        pairs.append((numbers[i], numbers[i+1]))
    pairs.sort(key=lambda  x:(x[0], x[1]))
    print(pairs)

    teams = [set(pairs.pop(0))]
    print(teams)
    for pair in pairs:
        for team in teams:
            if pair[0] in team:
                team.add(pair[1])
                break
            elif pair[1] in team:
                team.add(pair[0])
                break
        else:
            teams.append(set(pair))

    a = len(teams)
    cnt = 0
    for team in teams:
        cnt += len(team)
    b = N - cnt
    print("#{} {}".format(test_case, a+b))