#실패율

def solution(N, stages):
    leng=len(stages)
    answer=[]
    for i in range(1,N+1):

        if leng != 0:
            answer.append([i,stages.count(i)/leng])
            leng-=stages.count(i)
        else:
            answer.append([i,0])
        
    answer=sorted(answer,key=lambda x:x[1],reverse=True)
    answer=[i[0] for i in answer]
            
        
    return answer

N=5
stages=[2, 1, 2, 6, 2, 4, 3, 3]

solution(N, stages)
