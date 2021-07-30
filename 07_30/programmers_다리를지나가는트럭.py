### 다리를 지나가는 트럭

def solution(bridge_length, weight, truck_weight):
    bridge=[0]*bridge_length
    answer=0
    
    while True:
        if sum(truck_weight) == 0  and sum(bridge) ==0:
            break
        answer+=1
        del bridge[0]
        next=0
        if truck_weight:
            if sum(bridge) + truck_weight[0] <=weight:
                next=truck_weight[0]
                del truck_weight[0]
        bridge.append(next)
    return answer


bridge_length=2
weight=10
truck_weight=[7,4,5,6]

print(solution(bridge_length,weight,truck_weight))