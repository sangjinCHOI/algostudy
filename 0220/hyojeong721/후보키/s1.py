def make(main, sub, cnt):

    return cnt
def solution(relation):
    answer = 0
    student_num = {}
    name = {}
    major = {}
    grade = {}

    for i in range(len(relation)):
        student_num[i] = relation[i][0]
        name[i] = relation[i][1]
        major[i] = relation[i][2]
        grade[i] = relation[i][3]
    attribute = [student_num, name, major, grade]
    num = len(attribute)
    i = 0
    while i < num:
        temp = attribute.pop(0)
        if len(set(temp.values())) == len(relation):
            answer += 1
        else:
            attribute.append(temp)
        i += 1
    print(attribute)
    # 2가지 속성

    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))