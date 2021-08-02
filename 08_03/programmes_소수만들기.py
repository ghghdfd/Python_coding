from itertools import combinations
import math 

def check(s):
    for i in range(2,int(math.sqrt(s))+1):
        if s % i == 0:
            return False
    return True  

def solution(nums):
    answer=0
    nums_=list(combinations(nums, 3))
    nums_=list([sum(i) for i in nums_])
    
    for i in nums_:
        if check(i):
            answer+=1
            
    return answer

nums=[1,2,3,4]
solution(nums)