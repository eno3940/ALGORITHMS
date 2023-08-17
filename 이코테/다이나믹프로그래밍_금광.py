import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

for tc in range(int(input())):
    n,m = map(int, input().split())
    array = list(map(int, input().split()))
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index +m])
        index +=m
    # 다이나믹 프로그래밍 진행
    for j in range(1,m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0: left_up =0 #i가 0이면 왼쪽 위가 없으므로 그냥 0으로 처리
            else: left_up = dp[i-1][j-1] #i가 0이 아니면, 왼쪽 위가 있으므로 왼쪽 위 위치 반환
            # 왼쪽 아래에서 오는 경우
            if i == n-1: left_down =0 #i가 n-1이면 왼쪽 아래가 없으므로, 0으로 처리(어차피 max에서 선택x)
            else: left_down = dp[i+1][j-1]
            left = dp[i][j-1] #left는 늘 있으므로 그냥 처리
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1]) #맨 오른쪽 열 중에서 가장 큰 값을 고름
    print(result)
