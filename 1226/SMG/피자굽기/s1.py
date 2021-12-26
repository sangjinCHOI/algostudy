import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizzas = []
    for i in enumerate(list(map(int, input().split()))):
        pizzas.append(i)
    print(pizzas)
    fire = []
    for i in range(N):
        fire.append(pizzas.pop(0))
    print(fire)
    while len(fire) > 1:
        fire[0] = (fire[0][0], fire[0][1]//2)
        if fire[0][1] == 0:
            fire.pop(0)
            if pizzas:
                fire.append(pizzas.pop(0))
        else:
            fire.append(fire.pop(0))
    print(f'#{tc} {fire[0][0]+1}')


