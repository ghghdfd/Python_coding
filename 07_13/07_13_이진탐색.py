##이진탐색

def binary_search(array,target,start,end):
    if start>end:
        return None
    mid = (start+end)//2
    #찾았다면 인덱스 반환
    if array[mid]==target:
        return mid
    #중간점이 더 작다면 왼쪽을 확인
    elif array[mid]<=target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

n,target=list(map(int,input().split()))
result=binary_search(array,target,0,n-1)

if result == None:
    print('원소가 존재하지 않음')
else:
    print(result+1)


