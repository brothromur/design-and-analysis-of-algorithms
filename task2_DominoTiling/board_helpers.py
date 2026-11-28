def find_first_empty(board):
    n = len(board)
    for r in range(n):
        for c in range(n):
            if board[r][c] == 0:
                return (r, c)
    return None

def place_horizontal(board, domino_id):
    n = len(board)
    (r , c) = find_first_empty(board)
    if c + 1 < n and board[r][c + 1] == 0:
        board[r][c] = domino_id
        board[r][c + 1] = domino_id
        return board
    return None

def place_vertical(board, domino_id):
    n = len(board)
    (r , c) = find_first_empty(board)
    if r + 1 < n  and board[r + 1][c] == 0:
        board[r][c] = domino_id
        board[r + 1][c] = domino_id
        return board
    return None

def build_list(board, n):
    cells = {}
    for r in range(n):
        for c in range(n):
            k = board[r][c]
            if k != 'X':
                cells.setdefault(k, []).append((r, c))
    return [tuple(cells[k]) for k in sorted(cells)]
    


