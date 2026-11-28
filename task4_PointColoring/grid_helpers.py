def partner_of(p, pairs):
    for a, b in pairs:
        if a == p:
            return b
        if b == p:
            return a
    return None


def walkchain(start, h_pairs, v_pairs, visited, colors):
    visited[start] = True
    current = start
    next_axis = 'V' if partner_of(start, h_pairs) is None else 'H'

    while True:
        pairs = h_pairs if next_axis == 'H' else v_pairs
        neighbor = partner_of(current, pairs)
        if neighbor is None or visited[neighbor]:
            break

        if colors[current] == colors[neighbor]:
            colors[neighbor] = 'W' if colors[current] == 'B' else 'B'
        visited[neighbor] = True
        current = neighbor
        next_axis = 'V' if next_axis == 'H' else 'H'
    