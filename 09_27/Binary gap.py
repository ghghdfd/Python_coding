# binary gap

def solution(N):
    return max([len(x) for x in format(N, 'b').strip('0').split('1')])

n=529
print(solution(n))