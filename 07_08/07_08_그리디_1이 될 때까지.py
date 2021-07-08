### 1이 될 때까지 ###

n,k=map(int,input().split())

cnt=0
while True:
    if n % k == 0: # n이 k로 나눠지는 값이라면
        n=n//k #n은 k로 나눈 몫으로 변경
        cnt+=1 #연산 카운트 +1
        if n == 1: 
            break
    else: # 나눠지지 않는다면
        n-=1 #n에서 1 빼기
        cnt+=1 # 카운드 +1
    if n == 1: #n이 1과 같아지면 종료
        break
cnt