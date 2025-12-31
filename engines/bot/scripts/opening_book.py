import json
from collections import Counter, defaultdict
from pathlib import Path

import chess
import pandas as pd

HF_PARQUET = "hf://datasets/Lichess/chess-openings/data/train-00000-of-00001.parquet"

OUTPUT_JSON = Path("engines/bot/opening_book.json")

# 8 plies = about 4 moves for each side. Keeps the book small and fast.
MAX_PLIES = 8

def fen_key(board: chess.Board) -> str:
    return " ".join(board.fen().split()[:4])


def main():
    df = pd.read_parquet(HF_PARQUET, columns=["uci"])

    move_counts_by_position = defaultdict(Counter)

    for uci_line in df["uci"].dropna():
        moves = str(uci_line).split()
        board = chess.Board()

        for ply, move_uci in enumerate(moves[:MAX_PLIES]):
            key = fen_key(board)
            move_counts_by_position[key][move_uci] += 1

            # Stop if move is illegal in this position
            try:
                board.push_uci(move_uci)
            except ValueError:
                break

    # Choose the single most common move for each position
    opening_book = {}
    for key, counter in move_counts_by_position.items():
        best_move, _freq = counter.most_common(1)[0]
        opening_book[key] = best_move

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(opening_book, indent=2), encoding="utf-8")

    print(f"Saved {len(opening_book)} positions to {OUTPUT_JSON}")

if __name__ == "__main__":
    main()