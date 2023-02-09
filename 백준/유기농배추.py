import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

test=int(input())
def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if graph[x][y]==1:
        graph[x][y]=0
        dfs(x,y+1)
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y-1)
        return True

for _ in range(test):
    m,n,k=map(int,input().split())
    graph=[[0]*m for _ in range(n)]
    result=0
    for _ in range(k):
        y,x=map(int,input().split())
        graph[x][y]=1
    for i in range(n):
        for j in range(m):
            if dfs(i,j)==True:
                result+=1
    print(result)