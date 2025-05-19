from models.playingpiece import PlayingPiece
from models.piecetype import PieceType

class PlayingPieceO(PlayingPiece):

    def __init__(self):
        super().__init__(PieceType.O)


if __name__ == "__main__":
    p = PlayingPieceO()
    print(p.piece)

        