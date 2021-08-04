## 이중 우선 순위 큐

def solution(operations):
    temp=[]
    for i in operations:
        if i.startswith('I'):
            temp.append(int(i.split(' ')[1]))
            
        elif i.startswith('D'):
            if len(temp) ==0 :
                pass
            else:
                if i.split(' ')[1] == '1':
                    temp.remove(max(temp))
                elif i.split(' ')[1] == '-1':
                    temp.remove(min(temp))
                
        if len(temp) == 0:
            return [0,0]
        else:
            return temp
            
operations=	["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
solution(operations)
temp=[16]
temp.remove(max(temp))
temp
"D 1".split(' ')[1] == '1'
int('-5643')