import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    S = input()
    res = ''

    for c in range(len(S)):
        # 대문자이면
        num = ord(S[c])
        if 64 < num < 91:
            if chr(num + 32) in S:
                res += chr(num)
        # 소문자이면
        else:
            if chr(num - 32) in S:
                res += chr(num - 32)

    if len(res) == 0:
        print('NO')
    else:
        print(max(res))