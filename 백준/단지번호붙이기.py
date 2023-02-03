import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph=[]
for i in range(N):
    graph.append(list(map(int,input().rstrip())))
block_num = []
temp=0
def dfs(x,y):
    global temp
    if x<0 or x >=N or y<0 or y>=N:
        return
    if graph[x][y]==1:
        graph[x][y]=0
        temp+=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
    return temp

for i in range(N):
    for j in range(N):
        if dfs(i,j)!=0:
            block_num.append(temp)
            temp=0
            
print(len(block_num))
block_num.sort()
print(block_num)
for num in block_num:
    print(num)