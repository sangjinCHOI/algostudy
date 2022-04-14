def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[1])
    print(routes)
    camera = routes[0][1]
    for i in range(1, len(routes)):
        if camera < routes[i][0]:
            answer += 1
            camera = routes[i][1]
            print(camera)


    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))