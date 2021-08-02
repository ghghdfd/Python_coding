###두 개 뽑아서 더하기

from itertools import combinations

def solution(numbers):
    
    numbers_=list(combinations(numbers, 2))
    
    return sorted(list(set([sum(i) for i in numbers_])))


num=[5,0,2,7]
solution(num)