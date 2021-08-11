##위장 


import collections
from functools import reduce

def solution(c):
    counts=collections.Counter([x[1] for x in c]).values()
    counts=[i+1 for i in counts]
    return reduce(lambda x,y:x*y, counts)-1


c=[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(c)