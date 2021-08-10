##모의고사


def solution(answers):
    answer = []
    a1=[1,2,3,4,5]
    a2=[2,1,2,3,2,4,2,5]
    a3=[3,3,1,1,2,2,4,4,5,5]
    c1,c2,c3=0,0,0

    for i in range(len(answers)):
        if a1[i % len(a1)]==answers[i]:
            c1+=1
        if a2[i % len(a2)]==answers[i]:
            c2+=1
        if a3[i % len(a3)]==answers[i]:
            c3+=1
    target=max(c1,c2,c3)
    
    if target==c1:
        answer.append(1)
    if target==c2:
        answer.append(2)
    if target==c3:
        answer.append(3)
        
    return answer

answers=[1,2,3,4,5]
solution(answers)