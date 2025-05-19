from tictactoe import TicTacToe

class Main:

    def main(self, username1, username2):
        game = TicTacToe()
        game.initialize_game(username1, username2)
        print(f"Winner : {game.start_game()}")


m = Main()
m.main("aman", "anmol")