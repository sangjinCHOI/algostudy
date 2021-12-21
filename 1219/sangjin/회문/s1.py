import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        tmp = list(' '.join(input()).split())
        arr.append(tmp)

    for x in range(N-M+1):
        for y in range(N-M+1):
            for i in range(x, x+M):
                word_h = ''
                word_v = ''
                for j in range(y, y+M):
                    word_h += arr[i][j]
                    word_v += arr[j][i]

                if word_h == word_h[::-1]:
                    result = word_h
                if word_v == word_v[::-1]:
                    result = word_v

    print("#{} {}".format(test_case, result))