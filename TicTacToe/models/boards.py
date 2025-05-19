from models.playingpiece import PlayingPiece


class Board:

    def __init__(self,n):
        self.board_size = n 
        self.board_layout = [[" " for c in range(self.board_size)] for r in range(self.board_size)]

    def get_empty_cells(self):

        empty_cells : list[tuple] = []    
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board_layout[i][j] == " ":
                    empty_cells.append((i,j))

        return empty_cells

    def add_piece(self, row:int, col:int, playingpiece: PlayingPiece):
        
        if self.board_layout[row][col] != " ":
            return False
        self.board_layout[row][col] = playingpiece
        return True
    
    def print_board(self):

        for i in range(self.board_size):
            for j in range(self.board_size):
                if isinstance(self.board_layout[i][j], PlayingPiece):
                    if j!=self.board_size-1:
                        print(f"{self.board_layout[i][j].piece}", end = "|")
                    else:
                         print(f"{self.board_layout[i][j].piece}")
                else:
                    if j!=self.board_size-1:
                        print(" ", end ="|")
                    else:
                        print(" ")
            if i!=self.board_size-1:
                print("-"*5)
        print("\n") 


if __name__ == "__main__":

    b = Board(3)
    b.print_board()