#부족 금액 계산하기

def solution(price, money, count):

    result=sum([(price*i) for i in range(1,count+1)])
    
    if result > money:
        return result-money
    else:
        return 0

price,money,count=3,20,4

solution(price,money,count)