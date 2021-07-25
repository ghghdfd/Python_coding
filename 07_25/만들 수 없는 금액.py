##만들 수 없는 금액

n=int(input())
data=list(map(int,input().split()))
data.sort()

target = 1
for i in data:
    #찾으면 종료
    if target < x:
        break
    target += i

print(target)