# 표절

n = int(input())
ary = sorted(list(map(float,input().split())))

answer = 0 
for i in range(n):
    l = i
    r = n
    while l<r:
        c = (l+r)//2
        if ary[i]>=ary[c]*(0.9):
            l = c + 1 
        else:
            r = c 
    answer += r-i-1
    
print(answer)