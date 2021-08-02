#가운데 글자 가져오기

def solution(s):
    answer = ''
    leng=len(s)
    
    if leng < 3:
        answer=s
    else:
        if leng % 2 == 0:
            answer=s[leng//2-1:leng//2+1]
        else:
            answer=s[leng//2]
        
    return answer

s="abcde"
solution(s)