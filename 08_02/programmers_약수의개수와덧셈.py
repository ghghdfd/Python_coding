##약수의 개수와 덧셈

def solution(left,right):
    answer=0

    for i in range(left,right+1):
        cnt=0
        for j in range(1,i+1):
            if i % j == 0:
                cnt+=1
            else:
                pass

        if cnt % 2 == 0:
            answer+=i
        else:
            answer-=i
    return answer

left,right=13,17
solution(left, right)



### 제곱수의 약수는 홀수라는 정보를 이용한 풀이

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

left,right=13,17
solution(left, right)