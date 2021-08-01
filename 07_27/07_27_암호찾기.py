#암호 찾기

from itertools import combinations

vowels=('a','e','i','o','u')
l,c=map(int,input().split(' '))

array=input().split(' ')
array.sort()

for i in combinations(array,1):
    count=0
    for j in i:
        if i in vowels:
            count +=1
    if count >=1 and count <=1 -2:
        pinrt(''.join(i)) 
