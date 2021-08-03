#문자열 내림차순 정렬

#처음 풀이
def solution(s):
    up=[]
    low=[]
    for i in s:
        if i.isupper():
            up.append(i)
        else:
            low.append(i)
    up.sort(reverse=True)
    low.sort(reverse=True)
    
    answer=''.join(low+up)
    
    
    return answer


#간결한 풀이
def solution(s):

    answer=''.join(sorted(s,reverse=True))

    return answer

s="Zbcdefg"
solution(s)