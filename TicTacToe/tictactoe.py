from models.playingpiece import PlayingPiece
from models.players import Player
from models.boards import Board
from collections import deque
from models.playingpieceX import PlayingPieceX
from models.playingpieceO import PlayingPieceO


class TicTacToe:


    def __init__(self):
        self.players = deque()
    
    def initialize_game(self, player1_name, player2_name, n=3):
        self.gameboard = Board(n)
        player1 = Player(player1_name,PlayingPieceX())
        player2 = Player(player2_name, PlayingPieceO())
        self.players.append(player1)
        self.players.append(player2)

    def start_game(self):

        nowinner:bool = True
        
        while nowinner:
            
            free_cells = self.gameboard.get_empty_cells()

            if not free_cells:
                nowinner = False 
                continue

            player_turn = self.players.popleft()
            pos_inp = input("Enter the place you want to insert a piece")
            pos_inp = pos_inp.split(",")
            pos_inp = [int(ip.strip()) for ip in pos_inp]
            if not self.gameboard.add_piece(pos_inp[0], pos_inp[1], player_turn.playingpiece):
                print("Enter valid position")
                self.players.appendleft(player_turn)
                continue
            self.gameboard.print_board()
            winner:bool = self.isThereWinner(pos_inp[0], pos_inp[1], player_turn.playingpiece.piece)

            if winner:
                return f"{player_turn.username} wins"
            self.players.append(player_turn)
        return "tie"

    def isThereWinner(self, row, col , piece):
        
        #row check
        row_result = all(self.gameboard.board_layout[row][i] != " " and self.gameboard.board_layout[row][i].piece == piece for i in range(self.gameboard.board_size))

        #col check
        col_result = all(self.gameboard.board_layout[i][col] != " " and self.gameboard.board_layout[i][col].piece == piece for i in range(self.gameboard.board_size))

        #diagonal check
        if row==col:
            diag_res = all(self.gameboard.board_layout[i][i] != " " and self.gameboard.board_layout[i][i].piece == piece for i in range(self.gameboard.board_size))
        else:
            diag_res = False

        #anti diagonal check
        antidiag_res = all(self.gameboard.board_layout[i][self.gameboard.board_size-1-i] != " " and self.gameboard.board_layout[i][self.gameboard.board_size-1-i].piece == piece for i in range(self.gameboard.board_size))

        return row_result or col_result or diag_res or antidiag_res


if __name__ == "__main__":

    game = TicTacToe()
    game.initialize_game("aman", "anmol")
    print(game.start_game())
            

