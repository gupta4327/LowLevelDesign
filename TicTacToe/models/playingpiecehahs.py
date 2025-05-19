from models.piecetype import PieceType
from models.playingpiece import PlayingPiece

class PlayingPieceHahs(PlayingPiece):

    def __init__(self):
        super().__init__(PieceType.hahs)


