from .evaluation import get_evaluation

INFINITY = float("inf")

def minimax(board, depth: int, alpha: float, beta: float, is_maximizing: bool) -> int:
    # Base case: stop searching deeper
    if depth == 0 or board.is_game_over():
        return get_evaluation(board)

    if is_maximizing:
        best_score = -INFINITY

        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth - 1, alpha, beta, is_maximizing=False)
            board.pop()

            # keep the best score found so far
            best_score = max(best_score, score)

            alpha = max(alpha, score)

            if beta <= alpha:
                break

        return best_score

    else:
        best_score = INFINITY

        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth - 1, alpha, beta, is_maximizing=True)
            board.pop()

            best_score = min(best_score, score)
            beta = min(beta, score)

            if beta <= alpha:
                break

        return best_score