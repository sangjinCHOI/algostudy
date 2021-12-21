import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    word = list(input())

    while True:
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                word.pop(i)
                word.pop(i)
                break
        else:
            break

    print("#{} {}".format(test_case, len(word)))