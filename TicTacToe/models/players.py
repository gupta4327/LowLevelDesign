from models.playingpiece import PlayingPiece

class Player:

    def __init__(self, username:str, playingpiece: PlayingPiece):

        self.username = username
        self.playingpiece = playingpiece

    def get_playing_piece(self):
        return PlayingPiece.piece
    
    def get_username(self):
        return self.username
    
    def _set_playing_piece(self, playingpiece : PlayingPiece):
        self.playingpiece = playingpiece

    def _set_username(self, username:str):
        self.username = username

