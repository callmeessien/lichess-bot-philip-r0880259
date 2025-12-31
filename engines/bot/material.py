import chess

PIECE_VALUE = {
    chess.PAWN: 100,
    chess.KNIGHT: 310,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000,
}

# Go through each piece type and count them for each color
def get_material(board: chess.Board) -> int:
    white_score = 0
    black_score = 0

    for piece_type, value in PIECE_VALUE.items():
        white_count = len(board.pieces(piece_type, chess.WHITE))
        black_count = len(board.pieces(piece_type, chess.BLACK))

        white_score += white_count * value
        black_score += black_count * value

    return white_score - black_score