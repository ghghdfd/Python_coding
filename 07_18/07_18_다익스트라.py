## 다익스트라

import sys
input=sys.stdin.readline
INF=int(1e9)

#노드, 간선 수 입력
n.m = map(int,input().split())
# 시작 노드
start=int(input())
#각 노드 연결 정보 리스트
graph=[[] for i in range(n+1)]
#방문했다면 체크하는 리스트
visited=[False]*(n+1)
#최단 거리 테이블 모두 무한으로 초기화
distance=[INF]*(n+1)

#간전 정보 입력
for _ in range(m):
    a,b,c=map(int,input().split())
    #a노드에서 b노드로 가는 비용이 c
    graph[a].append((b,c))

#미방문 노드에서 최단 거리가 짧은 노드
def get_smallest_node():
    min_value=INF
    index=0 
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index +=1
    return index

def dijkstra(start):
    distance[start]=0
    visited[start]=True
    for j in graph[start]:
        distance[j[0]]=j[1]
    #시작 노드 제외한 전체 노드에 대한 반복
    for i in range(n-1):
        #현재 최단 거리가 가장 짧은 노드 꺼내서 방문 처리
        now=get_smallest_node()
        visited[now]=True
        #다른 연결 노드를 확인
        for j in graph[now]:
            cost=distance[now] + j[1]
            #현재 노드 거쳐 다른 노드 가는 거리가 더 짧다면
            if cost < distance[j[0]]:
                distance[j[0]]=cost

#다익스트라 실행
dijkstra(start)

#모든 노드 가기위한 최단 거리 출력
for i in range(1,n+1):
    #도달 못하면 inf 출력
    if distance[i]==INF:
        print('INFINITY')
    else:
        print(distance[i)