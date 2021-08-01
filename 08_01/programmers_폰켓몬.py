##폰켓몬

def solution(nums):
    
    possible = len(set(nums))
    
    if possible >= len(nums)//2:
        answer = len(nums)//2
    else:
        answer = possible
        
    return answer

nums=[3,1,2,3]

solution(nums)