# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys
sys.stdin = open('input.txt')

def solution(S, C):
    res = 0
    # write your code in Python 3.6
    i = 0
    while i < len(S):
        cost_lst = [C[i]]
        k = i+1
        while k < len(S) and S[k] == S[i]:
            cost_lst.append(C[k])
            k += 1


        if len(cost_lst) > 1:
            max_cost = max(cost_lst)
            cost_lst.remove(max_cost)
            for c in cost_lst:
                res += c
        if k == len(S):
            break
        i += 1
    print(res)

T= int(input())
for tc in range(1, T+1):
    S = input()
    C = list(map(int, input().split()))

    solution(S, C)
