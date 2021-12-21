import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    str1 = input()
    str2 = input()
    print(str1,str2)
    res = {}
    for alpa in str1:
        cnt = str2.count(alpa)
        res[alpa] = cnt
    print(res)

    val_lst = list(res.values())
    max_num = max(val_lst)
    print("#{} {}".format(tc, max_num))
