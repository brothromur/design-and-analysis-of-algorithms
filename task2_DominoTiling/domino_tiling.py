from board_helpers import *

def tile_dominoes(n, missing1, missing2):
    # If the given dimensions are odd, removing 2 tiles of opposite colors will ALWAYS result in no valid boards, exit early    
    if n % 2 == 1:
        return (False ,[])
    
    board = [[0] * n for _ in range(n)]       
    board[missing1[0]][missing1[1]] = 'X'
    board[missing2[0]][missing2[1]] = 'X'

    stack = [[board, 0]]
    while stack:
        board, tried = stack[-1] # tried is a tracker, 0 means we haven't tried horizontal placement, 1 is vertical, 2 is we've tried both
        
        if find_first_empty(board) == None:
            return (True, build_list(board, n))

        if tried == 0:
            stack[-1][1] = 1
            new_board = place_horizontal([row[:] for row in board], len(stack)) # The loop in the function call is done to copy the board instead of editing it directly
            if new_board != None:
                stack.append([new_board, 0])
                
        elif tried == 1:
            stack[-1][1] = 2
            new_board = place_vertical([row[:] for row in board], len(stack))
            if new_board != None:
                stack.append([new_board, 0  ])
                
        else:
            stack.pop()
            
    return (False, [])
        