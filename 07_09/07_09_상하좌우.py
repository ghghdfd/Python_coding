#구현

n=int(input())
x,y=1,1
plans=input().split()

#이동방향
dx = [0,0,-1,-1]
dy = [-1,1,0,0]
move=['L','R','U','D']

#이동방향 확인
for plans in plans:
    #이동 후 좌표 구하기
    for i in range(len(move)):
        if plans == move[i]:
            nx = x+dx[i]
            ny = x+dy[i]
    #공간 벗어나면 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    #이동하기
    x,y = nx, ny

print(x,y)