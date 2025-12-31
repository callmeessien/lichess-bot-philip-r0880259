import chess
from .material import get_material
from . import positions

CHECKMATE_SCORE = 9999

# Piece-Square Table (PST)
PST = {
    chess.PAWN: positions.pawn,
    chess.KNIGHT: positions.knight,
    chess.BISHOP: positions.bishop,
    chess.ROOK: positions.rook,
    chess.QUEEN: positions.queen,
    chess.KING: positions.king,
}

def get_piece_square_score(board: chess.Board) -> int:
    score = 0

    for piece_type, table in PST.items():
        for sq in board.pieces(piece_type, chess.WHITE):
            score += table[sq]

        for sq in board.pieces(piece_type, chess.BLACK):
            score -= table[chess.square_mirror(sq)]

    return score

def get_evaluation(board: chess.Board) -> int:
    if board.is_checkmate():
        return -CHECKMATE_SCORE if board.turn == chess.WHITE else CHECKMATE_SCORE

    if board.is_stalemate() or board.is_insufficient_material():
        return 0

    material_score = get_material(board)
    positional_score = get_piece_square_score(board)

    return material_score + positional_score