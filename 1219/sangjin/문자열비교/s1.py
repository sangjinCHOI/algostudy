import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    str1 = input()
    str2 = input()

    if str1 in str2:
        result = 1
    else:
        result = 0

    print("#{} {}".format(test_case, result))