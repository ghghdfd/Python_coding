# 숫자 문자열과 영단어

def solution(s):
    #알파벳과 숫자 매칭 딕셔너리 생성
    dict={}
    eng=['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(10):
        dict[eng[i]]=i
    
    #정답 문자열과 알파벳 임시 문자열 생성
    result=''
    en=''

    for i in s: 
        if i.isdigit(): #문자열이 숫자라면
            result+=i #정답에 연결
        elif i.isalpha(): #알파벳이라면
            en+=i #알파벳 문자열에 연결
            if en in dict.keys(): #연결된 문자열이 딕셔너리 키에 존재한다면
                result+=str(dict[en]) #정답에 해당 밸류값 연결
                en='' #다른 알파벳 위해 임시 문자열 초기화

    return int(result)
            
s="one4seveneight"
solution(s)
