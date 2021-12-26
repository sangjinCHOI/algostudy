import sys
sys.stdin = open('input.txt')

def hwaduck(n, pizza):
    #(화덕 번호, 치즈양, 피자번호)
    q = []
    for i in range(n):
        q.append([i+1, pizza[i], i])

    new_piz_num = n
    while q:
        if len(q) == 1:
            return q.pop()[2] + 1

        temp = q.pop(0)
        idx = temp[0]
        cheeze = temp[1] // 2
        piz_num = temp[2]
        temp = [idx, cheeze, piz_num]

        if cheeze > 0:
            q.append(temp)
        else:
            if new_piz_num < len(pizza):
                q.append([idx, pizza[new_piz_num], new_piz_num])
                new_piz_num += 1



T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    pizza = list(map(int, input().split()))

    print("#{}".format(tc), hwaduck(n, pizza))
