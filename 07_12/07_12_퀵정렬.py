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


array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort2(array):
    #리스트가 하나 이하의 원소면 종료
    if len(array)<=1:
        return array

    pivot = array[0] #피벗은 첫 원소
    tail = array[1:] #피벗을 제외한 리스트

    left_side=[x for x in tail if x <= pivot] #분할된 왼쪽부분
    right_side=[x for x in tail if x > pivot] #오른쪽 부분

    #분할 후 왼쪽, 오른쪽에서 각각 정렬하고 전체 리스트 반환
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

print(quick_sort2(array))