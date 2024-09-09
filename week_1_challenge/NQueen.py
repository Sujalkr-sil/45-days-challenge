def solveNQueens(n):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
               return False
        return True

    def solve(row, board):
        if row == n:
            solution = []
            for i in range(n):
                row_str = '.' * board[i] + 'Q' + '.' * (n - board[i] - 1)
                solution.append(row_str)
            result.append(solution)
        else:
            for col in range(n):
                if is_valid(board, row, col):
                    board[row] = col
                    solve(row + 1, board)
                    board[row] = -1 

    result = []
    board = [-1] * n  
    solve(0, board)
    return result

n = 4
solutions = solveNQueens(n)
sol=[]
for solution in solutions:
    sol.append(solution)
print(sol)