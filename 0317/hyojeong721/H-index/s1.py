def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    print(citations)
    answer = max(list(map(min, enumerate(citations, start=1)))))
    return answer

def solution(citations):
  sorted_citations = sorted(citations, reverse=True) # [6,5,3,1,0]
  for i in range(len(sorted_citations)):
    if sorted_citations[i] <= i:
      return i
  return len(sorted_citations)

citations =	[3, 0, 6, 1, 5]
# citations =	[10, 10,10,10,10]
# citations =	[41, 24]
print(solution(citations))
