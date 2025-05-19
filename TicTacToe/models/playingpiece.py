from abc import ABC
from models.piecetype import PieceType

class PlayingPiece(ABC):

    def __init__(self, piece : PieceType):
        self.piece = piece


