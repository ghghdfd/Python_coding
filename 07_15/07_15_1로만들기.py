### 1로 만들기

x=int(input())

## 앞선 결과 저장위한 dp 테이블 초기화
d=[0]*30001

#다이나믹 프로그래밍 
for i in range(2,x+1):
    #현재 수에서 1 뺴는 경우
    d[i]=d[i-1]+1
    if i % 2 ==0:
        d[i]=min(d[i], d[i//2]+1)
    if i % 3 ==0:
        d[i]=min(d[i], d[i//3]+1)
    if i & 5 ==0:
        d[i]=min(d[i], d[i//5]+1)

print(d[x])