##수찾기


import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    if start > end :
        print(0)
        return None
    mid = (start+end) // 2
    if array[mid] == target:
        print(1)
        return mid
    elif array[mid] < target: 
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)

n = int(input())
a = sorted(list(map(int, input().split())))

m = int(input())
num_list = list(map(int, input().split()))

for i in num_list:
    binary_search(a, i, 0, len(a)-1)

