def print_board(board):
    print('---------')
    for row in board:
        print('|', end=' ')
        for cell in row:
            print(cell if cell != '' else ' ', end=' | ')
        print('\n---------')

def check_winner(board):
    # בדיקת שורות ועמודות
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '':
            return board[0][i]
    # בדיקת אלכסונים
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

def is_full(board):
    for row in board:
        if '' in row:
            return False
    return True

def tictactoe():
    board = [['' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        try:
            move = input(f"שחקן {current_player}, בחר שורה ועמודה (למשל, 1 2): ")
            row, col = map(int, move.strip().split())
            row -= 1
            col -= 1
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("יש לבחור מספרים בין 1 ל-3.")
                continue
            if board[row][col] != '':
                print("התא כבר תפוס. נסה שוב.")
                continue
            board[row][col] = current_player
        except Exception:
            print("קלט לא תקין. נסה שוב.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"נצחון ל-{winner}!")
            break

        if is_full(board):
            print_board(board)
            print("תיקו!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    tictactoe()