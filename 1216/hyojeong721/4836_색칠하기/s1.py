import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    box = [[0] * 10 for _ in range(10)]
    color_box = [list(map(int, input().split())) for _ in range(n)]
    print(color_box)
    res = 0
    for i in range(n):
        start_x = color_box[i][0]
        start_y = color_box[i][1]
        end_x = color_box[i][2]
        end_y = color_box[i][3]
        color = color_box[i][4]
        # 색칠영역 탐색
        for x in range(start_x, end_x+1):
            for y in range(start_y, end_y+1):
                # 기존 box 색상이 없거나 본인 색이랑 같으면 본인색 대입
                if box[x][y] == 0 or box[x][y] == color:
                    box[x][y] = color
                # 다른 색이 있으면 출력값 += 1
                else:
                    box[x][y] = 3
                    res += 1

    print('#{} {}'.format(tc, res))
