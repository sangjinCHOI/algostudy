import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    # str1 = list(set(list(''.join(input().split()))))
    str1 = list(set(input()))
    str2 = input()
    result = 0

    for x in str1:
        tmp = str2.count(x)
        if tmp > result:
            result = tmp

    print("#{} {}".format(test_case, result))

