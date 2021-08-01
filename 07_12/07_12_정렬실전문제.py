## 위에서 아래로

n=int(input())

array=[]
for i in range(n):
    array.append(int(input()))

array = sorted(array,reverse=True)

for i in arrat:
    print(i,end=' ')


## 성적이 낮은 순서로 학생 출력하기

n=int(input())

array=[]
for i in range(n):
    input_data=input().split()
    array.append((input_data[0],int(input_data[1])))

array=sorted(array,key=lambda student: student[1])

for student in array:
    print(student[0],end=' ')


## 두 배열의 원소 교체

n,k=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort() #배열 a는 오름차순
b.sort(reverse=True) #배열 b는 내림차순

for i in range(k): #k번까지 비교
    if a[i] < b[i]:
        a[i],b[i] = b[i],a[i]
    else:
        break
print(sum(a))
