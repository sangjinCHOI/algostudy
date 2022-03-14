import itertools
def primenumber(x):
    if x == 1:
        return False
    for i in range(2, x):	# 2부터 x-1까지의 모든 숫자
    	if x % i == 0:		# 나눠떨어지는게 하나라도 있으면 False
        	return False
    return True

def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        for t in itertools.permutations(numbers, i):
            temp = ''
            for num in t:
                temp += num
            if primenumber(int(temp)) and int(temp) not in answer:
                answer.append(int(temp))
    if 0 in answer:
        answer.remove(0)
    return len(answer)

numbers = "011"
print(solution(numbers))