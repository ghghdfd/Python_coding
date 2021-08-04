##124나라

def solution(n):

    arr=['1','2','4']
    
    if n<=3:
        return arr[n-1]
    else:
        q,r =divmod(n-1,3)
        return solution(q)+arr[r]

n=100
solution(n)