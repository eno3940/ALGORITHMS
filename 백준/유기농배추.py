import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

test=int(input())
for _ in range(test):
    m,n,k=map(int,input().split())
    graph=[[0]*m for _ in range(n)]
    # print(m,n,k)
    # print(graph)
    # print(len(graph))
    for _ in range(k):
        y,x=map(int,input().split())
        graph[x][y]=1
    print(graph)