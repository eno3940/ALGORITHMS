import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input().rstrip())))

from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y):
    queue=deque([(x,y)])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx= x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny <0 or ny >=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]= graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))