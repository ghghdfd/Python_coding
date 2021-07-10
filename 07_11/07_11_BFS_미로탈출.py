from collections import deque

n,m=map(int,input().spli())

#리스트 정보 입력
graph=[]
for i in range(n):
    graph[i]=list(map(int,input()))

#이동할 네 방향 정의 
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#bfs

def bfs(x,y):
    #큐 생성
    queue=deque()
    queue.append((x,y))
    #큐 빌 때까지 반복
    while queue:
        x,y=queue.popleft()
        #현 위치에서 방향 확인
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            #공간 벗어나면 무시
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            #벽이면 무시
            if graph[nx][ny]==0:
                continue
            #처음 방문인 경우만 최단거리기록
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    #가장 오른쪽 아래까지의 최단거리 반환
    return graph[n-1][m-1]

print(bfs(0,0))