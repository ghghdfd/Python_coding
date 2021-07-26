## 소수 판별 기본
def is_print(x):
    for i in range(2,x):
        if x % i == 0:
            return False
        
    return True

## 소수 판별 제곱근
import math

def is_prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

## 소수 판별 에라토스테네스의 체
import math

n=100 #2부터 1000까지 소수판별
array=[True for i in range(n+1)] #처음엔 모든 수가 소수

for i in range(2,int(math.sqrt(n))+1): #2부터 n의 제곱근까지 모두 확인 
    if array[i] == True: #i가 소수인 경우
        #i를 제외한 모든 i의 배수를 지우기
        j=2
        while i*j  <= n:
            array[i*j]=False
            j+=1
for i in range(2,n+1):
    if array[i]:
        print(i,end=' ')