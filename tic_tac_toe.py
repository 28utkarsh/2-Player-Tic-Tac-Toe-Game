from IPython.display import clear_output
class tic_tac_toe:
    def __init__(self):
        self.board_status = [[-1 for _ in range(3)] for _ in range(3)]
        self.O_pos = []
        self.X_pos = []    
        self.dict = {1:(2, 0), 2:(2, 1), 3:(2, 2), 4:(1, 0), 5:(1, 1),\
                   6:(1, 2), 7:(0, 0), 8:(0, 1), 9:(0, 2)}
        self.board_X = None
        self.board_O = None
        self.count_pos = 0
        self.filled_pos = {}
    def add_var(self, pos, var):
        while True:
            if pos not in self.filled_pos:
                cur = self.dict[pos]
                self.board_status[cur[0]][cur[1]] = 2 if var == 'X' else 3
                self.filled_pos[pos] = 'X' if var == 'X' else 'O'
                break
            else:
                print("Position ", pos," is being occupide with ", self.filled_pos[pos])
                pos = int(input("Please Enter another position to continue:"))
        self.count_pos += 1
        self.print_board()
        return self.check_win()
    def print_board(self):
        clear_output()
        print('------------------')
        for i in range(3):
            print('  ', end = '')
            for j in range(3):
                if self.board_status[i][j] != -1:
                    print('X' if self.board_status[i][j] == 2 else 'O', end = '')
                else:
                    print(' ', end = '')
                if j != 2:
                    print('  |  ', end = '')
            print('\n------------------')
        
    def check_win(self):
        for i in range(3):
            prod_X = 1
            prod_O = 1
            for j in range(3):
                prod_X *= self.board_status[i][j]
                prod_O *= self.board_status[i][j]
            if prod_X == 8:
                print("Congratulations ",self.board_X,". You have won the game")
                return 1
            elif prod_O == 27:
                print("Congratulations ",self.board_O,". You have won the game")
                return 1
        for i in range(3):
            prod_X = 1
            prod_O = 1
            for j in range(3):
                prod_X *= self.board_status[j][i]
                prod_O *= self.board_status[j][i]
            if prod_X == 8:
                print("Congratulations ",self.board_X,". You have won the game")
                return 1
            elif prod_O == 27:
                print("Congratulations ",self.board_O,". You have won the game")
                return 1
        prod_diag = self.board_status[0][0] * self.board_status[1][1] * self.board_status[2][2]
        if prod_diag == 8:
                print("Congratulations ",self.board_X,". You have won the game")
                return 1
        elif prod_diag == 27:
            print("Congratulations ",self.board_O,". You have won the game")
            return 1
        prod_diag = self.board_status[0][2] * self.board_status[1][1] * self.board_status[2][0]
        if prod_diag == 8:
                print("Congratulations ",self.board_X,". You have won the game")
                return 1
        elif prod_diag == 27:
            print("Congratulations ",self.board_O,". You have won the game")
            return 1
        return 0
if __name__ == '__main__':
    board = tic_tac_toe()
    board.board_X = input("Please enter the name of Player 1:")
    board.board_O = input("Please enter the name of Player 2:")
    while True:
        if board.count_pos % 2 == 0:
            pos = int(input(str(board.board_X)+', Please enter a position to make your move:'))
            win = board.add_var(pos, 'X')
        else:
            pos = int(input(str(board.board_O)+', Please enter a position to make your move:'))
            win = board.add_var(pos, 'O')
        if win == 1:
                c = input("Do you want to play again? Y/N?")
                if c == 'Y':
                    temp1 = board.board_X
                    temp2 = board.board_O
                    board = tic_tac_toe()
                    board.board_X = temp1
                    board.board_O = temp2
                else:
                    break
        if board.count_pos == 9:
            print(board.board_X,' vs ',board.board_O,': Result: Draw')
            c = input("Do you want to play again? Y/N?")
            if c == 'Y':
                temp1 = board.board_X
                temp2 = board.board_O
                board = tic_tac_toe()
                board.board_X = temp1
                board.board_O = temp2
            else:
                break
    x = input('\n----------------------------------------\nTHANK YOU\nPRESS ENTER TO EXIT')