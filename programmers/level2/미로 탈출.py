def solution(board):
    # O와 X의 갯수를 세는 함수
    def count_symbols(board):
        cnt_X = 0
        cnt_O = 0
        for row in board:
            for symbol in row:
                if symbol == "X":
                    cnt_X += 1
                elif symbol == "O":
                    cnt_O += 1
        return (cnt_X, cnt_O)
    cnt_X,cnt_O=count_symbols(board)
    # 누가 이겼는지?
    def check_win(board):
        winner=str()
        # 가로 방향으로 승리 확인
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != ".":
                winner+=board[i][0]

        # 세로 방향으로 승리 확인
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] != ".":
                winner+=(board[0][i])

        # 대각선 방향으로 승리 확인
        if board[0][0] == board[1][1] == board[2][2] != ".":
            winner+=(board[0][0])
        if board[0][2] == board[1][1] == board[2][0] != ".":
            winner+=(board[0][2])
        
        if "O" in winner and "X" in winner:
            return 0
        if len(winner)==1:
            return winner[0]
        if len(winner)==0:
            return None
        
    winner=check_win(board)
    
    # 이긴 사람이 2명 이상일 때
    if winner == False:
        return 0
    # O가 이겼을 때
    if winner == "O":
        if cnt_O ==(cnt_X+1):
            return 1
        else:
            return 0
    # X가 이겼을 때
    if winner == "X":
        if cnt_O == cnt_X:
            return 1
        else:
            return 0
    # 아무도 안이겼을 때
    if winner == None:
        if cnt_O == cnt_X or cnt_O == (cnt_X+1):
            return 1
        else:
            return 0
    
    
# print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))