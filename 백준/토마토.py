import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

#M은 상자의 가로 칸수
#N은 상자의 세로 칸수
m,n = map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
#1이 있는 위치 탐색 후 queue에다가 저장
from collections import deque
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            queue.append([i,j])
dx = [0,0,-1,1]
dy = [1,-1,0,0]

#bfs
def bfs():
    cnt=0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                graph[nx][ny]= graph[x][y]+1
                queue.append([nx,ny])
bfs()
answer=0
for i in graph:
    for j in i:
        if j==0: #bfs를 돌렸는데 안익은게 있으면 -1 출력하고 종료
            print(-1)
            exit(0)
    answer=max(answer,max(i))
print(answer-1) #첫 날 익은 토마토가 2. 즉 +1 씩 되어있으므로 -1