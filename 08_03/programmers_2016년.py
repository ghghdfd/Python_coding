#2016년

import datetime

def solution(a, b):
    day=['MON','TUE','WED','THU','FRI','SAT','SUN']
    dict={}

    for i in range(7):
        dict[day[i]]=i
    
    weekdy=datetime.datetime(2016,a,b).weekday()

    for i in dict.items():
        if weekdy==i[1]:
            answer=''.join(i[0])
            
    return answer

a,b=5,24
solution(a,b)
