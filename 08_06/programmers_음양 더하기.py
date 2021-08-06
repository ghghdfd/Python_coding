##음양 더하기

def solution(absolutes, signs):
    
    for i in range(len(signs)):
        if signs[i]==False:
            absolutes[i]=-(absolutes[i])
        else:
            pass
    
    return sum(absolutes)

absolutes, signs=[4,7,12],[True,False,True]
solution(absolutes, signs)