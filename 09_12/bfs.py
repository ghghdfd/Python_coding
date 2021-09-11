##bfs

import sys
from collections import deque

def bfs():
    q = deque()
    result = 0
    for i in range(1,node+1): 
        if visit[i] == 0: 
            visit[i] = 1
            q.append(i)
            result += 1
            while q:
                now = q.popleft()
                for j in graph[now]:
                    if visit[j] == 0:
                        visit[j] = 1
                        q.append(j)
    print(result)

if __name__ == "__main__":
    read = sys.stdin.readline
    node, line = map(int,read().split())
    graph = [[] * node for _ in range(node+1)]
    visit = [0] * (node+1)
    
    for i in range(line):
        start,end = map(int,read().split())
        graph[start].append(end)
        graph[end].append(start)
    bfs()

