##큰수만들기

#처음 조합으로 시도 시간초과
from itertools import combinations

def solution(number, k):
    perm=list(combinations(number,len(number)-k))
    answer = max([int(''.join(i)) for i in perm])
    return answer

#스택으로 재시도 성공
def solution(number, k):
    answer = ''
    stack = []
    for i in number:
        while stack and stack[-1] < i and k>0:
            k-=1
            stack.pop()
        stack.append(i)
    return "".join(stack[:len(stack)-k])


number="1231234"
solution(number,k=2)

