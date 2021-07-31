###프로그래머스_타겟 넘버


from itertools import product

def solution(numbers, target):

    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))

    return s.count(target)

numbers=[1,1,1,1,1]
target=3

print(solution(numbers,target))
