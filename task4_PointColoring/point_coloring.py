from grid_helpers import partner_of, walkchain


def point_coloring(n, points):
    # Input: integer n representing how many points there are, an array of tuples "points" representing xy-coordniates 
    # Output: list of 'B'/'W', one per point
    h_pairs = [] # Pairing points horizontally 
    v_pairs = [] # Pairing point vertically 
    colors = ['B'] * n
    visited = [False] * n
    
    # Sorting the points array by rows, that way they can properly be grouped into horizontal pairs first (also leaves out any points with no horizontal partner)
    order = sorted(range(n), key=lambda k: (points[k][1], points[k][0]))
    i = 0
    while i < n - 1:
        if points[order[i]][1] == points[order[i + 1]][1]:
            h_pairs.append((order[i], order[i + 1]))
            i += 2
        else:
            i += 1
            
    # Same sorting idea but vertically
    order = sorted(range(n), key=lambda k: (points[k][0], points[k][1]))
    i = 0
    while i < n - 1:
        if points[order[i]][0] == points[order[i + 1]][0]:
            v_pairs.append((order[i], order[i + 1]))
            i += 2
        else:
            i +=1
    
    # paths first: start from an end (a point missing at least one partner)
    for i in range(n):
        if not visited[i] and (partner_of(i, h_pairs) is None or partner_of(i, v_pairs) is None):
            walkchain(i, h_pairs, v_pairs, visited, colors)
    # whatever is left must be cycles
    for i in range(n):
        if not visited[i]:
            walkchain(i, h_pairs, v_pairs, visited, colors)

    return colors
    
    
