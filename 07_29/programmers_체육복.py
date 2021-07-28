##프로그래머스_체육복

def solution(n, lost, reserve):
    answer = 0
    set_reserve=set(reserve)-set(lost)
    set_lost=set(lost)-set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    answer+=n-len(set_lost)
            
    
    return answer


def solution(n,lost,reserve):
    r_reserve=[i for i in reserve if i not in lost]
    r_lost=[j for j in lost if j not in reserve]
    
    for i in r_reserve:
        f=i-1
        s=i+1
        if f in r_lost:
            r_lost.remove(f)
        elif s in r_lost:
            r_lost.remove(s)
            
    return n-len(r_lost)

