##퀵정렬

array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        #피벗보다 큰 데이터 찾을 떄까지 반복 
        while left <= end and array[left] <= array[pivot]:
            left +=1
        #피벗보다 작은 데이터 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -=1
        if left > right: #엇갈리면 작은 데이터와 피벗 교체
            array[right] ,array[pivot]=array[pivot],array[right]
        else: #아니면 작은 데이터와 큰 데이터 교체
            array[left], array[right]= array[right],array[left]
    #분할 후 왼쪽과 오른쪽에 각각 정렬 수헹
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array, 0, len(array)-1)

print(array)