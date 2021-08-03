#콜라즈 추측


def solution(num):
    cnt=0
    while True:
        if (cnt == 500) or (num==1):
            break

        if num % 2==0:
            num/=2
            cnt+=1
        elif num % 2 ==1:
            num=(num*3)+1
            cnt+=1
        
    if cnt==500:
        return -1
    else:
        return cnt


n=6
solution(n)