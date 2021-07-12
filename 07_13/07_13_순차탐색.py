##순차탐색
def sequensial_search(n,target,array):
    #원소 하나씩 확인
    for i in range(n):
        if array[i] == target:
            return i+1

input_data=input().split()
n=int(input_data[0])
target=input_data[1]
array=input().split()

print(sequensial_search(n,target,array))