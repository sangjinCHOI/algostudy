import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    word = input()

    while True:
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                word = word[:i] + word[i+2:]
                break
        else:
            break

    print("#{} {}".format(test_case, len(word)))