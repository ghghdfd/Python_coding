def febo(x):
    if x ==1 or x ==2:
        return 1
    return febo(x-1)+febo(x-2)

print(febo(4))


##  메모이제이션

# 한번 계산한 결과를 리스트 초기화
d=[0]*100

def fibo(x):
    #종료조건
    if x ==1 or x ==2:
        return 1
    #이미 계산한 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    #아직 계산 전이면 점화식에따라 반환
    d[x]=fibo(x-1)+fibo(x-2)
    return d[x]

print(fibo(4))