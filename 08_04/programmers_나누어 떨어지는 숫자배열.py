##나누어 떨어지는 숫자배열

def solution(arr, divisor):
    answer = []
    for i in arr:
        cnt=0
        if i % divisor ==0:
            answer.append(i)
            
    if len(answer)!=0:
        return sorted(answer)
    else:
        return [-1]

arr=[5,9,7,10]
divisor=5
solution(arr,divisor)