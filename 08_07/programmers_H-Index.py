##H-Index
from collections import deque


def solution(citations):
    citations.sort()
    answer=len(citations)
    que=deque(citations)
    while que:
        h=0
        for i in que:
            if i >= answer:
                h+=1
            if answer <= h:
                return answer
        answer-=1
    return answer

citations=[3, 0, 6, 1, 5]
solution(citations)