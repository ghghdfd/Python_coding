### 큰 수의 법칙 ###
#N,M,K
#K는 항상 M보다 작거나 같음
#n,m,k 입력

n,m,k = map(int,input().split())

#n개의 수를 공백으로 구분해 입력
data=list(map(int,input().split()))
data.sort()

first=data[n-1] # 가장 큰 수
second=data[n-2] # 두번째 큰 수

answer=0
print(n,m,k)
while True:
    for i in range(k):
        if m == 0: #m이 0이면 반복문 탈출
            break
        answer+=first #정답에 가장 큰 수 더하기
        m-=1 #하나 더할때마다 1씩 차감
    if m == 0: #m이 0이면 반복문 탈출
        break
    answer += second #k번 가장 큰 수 더했으면
                     # 두번째 큰수 한번 더하고
    m -=1 # 하나 더할때마다 1씩 차감

print(answer)


n,m,k = map(int,input().split())
data= list(map(int,input().split()))

data.sort()

first=data[n-1]
second=data[n-2]

answer=0

while True:
    if m == 0:
        break
    for i in range(k):
        answer += first
        m -=1
    if m == 0:
        break
    answer += second
    m-=1

print(answer)
