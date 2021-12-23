import sys
sys.stdin = open('input.txt')

T = int(input())

def fight(n1, n2):
    if card[n1] == 1 and card[n2] == 2:
        return n2
    elif card[n1] == 1 and card[n2] == 3:
        return n1
    elif card[n1] == 2 and card[n2] == 1:
        return n1
    elif card[n1] == 2 and card[n2] == 3:
        return n2
    elif card[n1] == 3 and card[n2] == 1:
        return n2
    elif card[n1] == 3 and card[n2] == 2:
        return n1

def dc(l):
    if len(l) == 2:
        return
    dc(l[:len(l)//2])
    dc(l[len(l)//2+1:])




for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    students = [i for i in range(N)]
