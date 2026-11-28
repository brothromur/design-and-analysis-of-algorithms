from domino_tiling import tile_dominoes

print("2x2, missing (0,0,(1,1))", tile_dominoes(2, (0, 0), (1, 1)))   # expect (False, [])
print("4x4, missing (0,0),(0,1):", tile_dominoes(4, (0, 0), (0, 1)))
print("8x8, missing (1,0),(3,1)", tile_dominoes(8, (1, 0), (3, 1)))   # expect True, needs backtracking
print("5x5 is an odd board, false right away", tile_dominoes(5, (0, 0), (0, 1)))   # expect (False, [])