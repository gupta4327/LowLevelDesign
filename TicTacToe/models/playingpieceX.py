from models.playingpiece import PlayingPiece
from models.piecetype import PieceType


class PlayingPieceX(PlayingPiece):

    def __init__(self):
        super().__init__(PieceType.X)

