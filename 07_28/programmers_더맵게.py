###프로그래머스_더맵게

import heapq

def solution(s,K):
    answer=0
    heapq.heapify(s)
    while True:
        min1=heapq.heappop(s)
        if min1 >= K:
            break
        if len(s) == 0:
            return -1

        min2=heapq.heappop(s)
        heapq.heappush(s,(min1+(min2*2)))
        answer+=1

    return answer

    
s=[1, 2, 3, 9, 10, 12]
K=7
print(solution(s,K))