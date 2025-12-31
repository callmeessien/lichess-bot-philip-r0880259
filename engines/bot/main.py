import chess
from .minimax import minimax
from .opening import play_opening

INF = float("inf")

def get_move(board, depth: int):
    opening_move = play_opening(board)
    if opening_move:
        print("PLAYING OPENING MOVE:", opening_move)
        return opening_move

    top_move = None

    if board.turn == chess.WHITE:
        top_eval = -INF
    else:
        top_eval = INF

    for move in board.legal_moves:
        board.push(move)

        # after push(), board.turn is the opponent
        eval_score = minimax(board, depth - 1, -INF, INF, board.turn)

        board.pop()

        # after pop(), board.turn is back to the player we are choosing for
        if board.turn == chess.WHITE:
            if eval_score > top_eval:
                top_eval = eval_score
                top_move = move
        else:
            if eval_score < top_eval:
                top_eval = eval_score
                top_move = move

    print("CHOSEN MOVE:", top_move, "WITH EVAL:", top_eval)
    return top_move