### 숫자카드게임 ###

n,m=map(int,input().split()) #행, 열 입력

result=0
for i in range(n): #행 수만큼 반복
    data=list(map(int,input().split())) # 배열 정보 입력

    min_v=min(data) #배열 중 가장 작은 값

    result=max(result,min_v) # result 초기값과 비교해서 높은게 정답으로

print(result)

## 내 풀이 (이중 반복문)
answer=[]  
for i in range(n):
    data=list(map(int,input().split()))
    for j in data:
        if j == min(data):
            answer.append(j)
            break
print(max(answer))
