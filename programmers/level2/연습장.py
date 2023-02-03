import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline
def dfs(x,y):
    if x <= -1 or x>=n or y <= -1 or y>=m:
        return False
    if graph[x][y] ==0:
        graph[x][y] =1

        dfs(x-1 , y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip()))) #백준에는 rstrip필요 x
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j )==True:
            result +=1
print(result)