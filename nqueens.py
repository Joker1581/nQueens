#Check whether the current place is valid
#Parameters: row: current row column: current column queen_position: set of queen position 
def is_valid(row, column, queen_position):
    for k in range(row):
        if queen_position[k] == column or abs(k - row) == abs(queen_position[k] - column):
            return False
    return True

def n_queens(row, queen_position, n, sol_set):
    if row == n:
        sol_set.append(queen_position)
        print(queen_position)
        return 
    for i in range(n):
        if is_valid(row, i, queen_position):
            queen_position[row] = i
            n_queens(row + 1, queen_position, n, sol_set)
            queen_position[row] = 0
    
if __name__ == "__main__":
    n = int(input("请输入皇后的数量: "))
    queen_position = [0 for _ in range(n)]
    row = 0
    sol_set = list()
    n_queens(row, queen_position, n, sol_set)
    print(len(sol_set))