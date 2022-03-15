import sys
sys.stdin = open('sample_input.txt', 'r')
import itertools

def sit(ent, person, position):
    pas = True
    res = 0
    while person != 0:
        i = 0
        cnt = 1
        while pas:
            if 0 <= ent+i < len(position) and position[ent+i] == 0:
                position[ent + i] = cnt
                res += cnt
                break
            elif 0 <= ent-i < len(position) and position[ent-i] == 0:
                position[ent - i] = cnt
                res += cnt
                break
            i += 1
            cnt += 1
        person -= 1

    return res


T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    gates = []
    for i in range(3):
        gates.append(list(map(int, input().split())))
    answer = 9999999999999999
    for j in itertools.permutations([0,1,2], 3):
        position = ['x'] + [0 for i in range(N)]
        res = 0
        for gate_idx in j:
            res += sit(gates[gate_idx][0], gates[gate_idx][1], position)
            if answer < res:
                break
        if answer > res:
            answer = res
        sum(position[1:])
    print("#{} {}".format(test_case, answer))
