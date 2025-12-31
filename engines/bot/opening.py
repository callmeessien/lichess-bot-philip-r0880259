import json
from pathlib import Path
import chess

_BOOK_PATH = Path(__file__).with_name("opening_book.json")

if _BOOK_PATH.exists():
    OPENING_BOOK = json.loads(_BOOK_PATH.read_text(encoding="utf-8"))
else:
    OPENING_BOOK = {}

def fen_key(board: chess.Board) -> str:
    return " ".join(board.fen().split()[:4])

def play_opening(board: chess.Board):
    key = fen_key(board)
    move_uci = OPENING_BOOK.get(key)
    if not move_uci:
        return None

    move = chess.Move.from_uci(move_uci)

    if move in board.legal_moves:
        return move

    return None