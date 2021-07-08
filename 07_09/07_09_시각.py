# 구현 2

h=int(input())

cnt=0

for i in range(h+1):

    for j in range(60):

        for k in range(60):
            
            # 3 포함이면 cnt + 1
            if '3' in str(i) +str(j) +str(k):
                cnt+=1