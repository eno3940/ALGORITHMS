import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input().rstrip())))

def dfs(x,y):
    if x<= -1 or x >=n or y<= -1 or y>=m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True #if 조건 안에 들어가면 dfs함수가 True 반환
    return False #if 조건안에 들어가지 않으면 dfs함수가 False반환
result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True: #True반환된 횟수만큼 result 1추가
            result +=1
print(result)