def solution(files):
    answer = []
    temp_dic = {}
    idx = -1
    for f in files:
        i = 0
        while f[i].isdigit():
            header = f[:i]
            temp = f[i:]
            i += 1
        j = 0
        print(header, temp)
        # while temp[j].isdigit() == False:
        #     number = temp[:j]
        #     tail = temp[j:]
        #     j += 1
        # print(header, number, tail)

    return answer

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print("answer:", solution(files))
