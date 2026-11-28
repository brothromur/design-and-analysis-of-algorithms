from functools import lru_cache


def break_all_squares(n):
    size = 2 * n + 1

    # 1) Number every toothpick (cells where row + col is odd)
    toothpicks = []      # toothpicks[i] = (row, col)
    index_of = {}        # (row, col) -> i
    for r in range(size):
        for c in range(size):
            if (r + c) % 2 == 1:
                index_of[(r, c)] = len(toothpicks)
                toothpicks.append((r, c))
    E = len(toothpicks)

    # 2) List every square as a list of its toothpick numbers
    squares = []
    for k in range(1, n + 1):               # square size
        for r in range(n - k + 1):          # top-left corner
            for c in range(n - k + 1):
                edges = []
                for t in range(k):
                    edges.append(index_of[(2 * r, 2 * (c + t) + 1)])        # top
                    edges.append(index_of[(2 * (r + k), 2 * (c + t) + 1)])  # bottom
                    edges.append(index_of[(2 * (r + t) + 1, 2 * c)])        # left
                    edges.append(index_of[(2 * (r + t) + 1, 2 * (c + k))])  # right
                squares.append(edges)
    S = len(squares)

    # 3) For each toothpick: which squares it breaks, which squares end at it
    breaks = [set() for _ in range(E)]
    last_chance = [set() for _ in range(E)]
    for s in range(S):
        for e in squares[s]:
            breaks[e].add(s)
        last_chance[max(squares[s])].add(s)

    # 4) DP with memoization
    @lru_cache(maxsize=None)
    def best(i, alive):
        if i == E:
            return 0
        # Option 1: remove toothpick i
        answer = 1 + best(i + 1, alive - breaks[i])
        # Option 2: keep it, only if no alive square needs it
        if not (alive & last_chance[i]):
            answer = min(answer, best(i + 1, alive))
        return answer

    all_squares = frozenset(range(S))
    best(0, all_squares)

    # 5) Rebuild the decisions
    removed = []
    alive = all_squares
    for i in range(E):
        can_keep = not (alive & last_chance[i])
        if can_keep and best(i + 1, alive) == best(i, alive):
            continue                        # keep toothpick i
        removed.append(toothpicks[i])       # remove toothpick i
        alive = alive - breaks[i]
    return removed


# ---------- helpers & tests ----------
def draw_board(n, removed):
    size = 2 * n + 1
    gone = set(removed)
    for r in range(size):
        line = ""
        for c in range(size):
            present = (r, c) not in gone
            if r % 2 == 0 and c % 2 == 0:
                line += "+"
            elif r % 2 == 0:
                line += "---" if present else "   "
            elif c % 2 == 0:
                line += "|" if present else " "
            else:
                line += "   "
        print(line)


def is_valid(n, removed):
    gone = set(removed)
    for k in range(1, n + 1):
        for r in range(n - k + 1):
            for c in range(n - k + 1):
                broken = False
                for t in range(k):
                    if ((2 * r, 2 * (c + t) + 1) in gone or
                            (2 * (r + k), 2 * (c + t) + 1) in gone or
                            (2 * (r + t) + 1, 2 * c) in gone or
                            (2 * (r + t) + 1, 2 * (c + k)) in gone):
                        broken = True
                        break
                if not broken:
                    return False
    return True


if __name__ == "__main__":
    for n in range(2, 5):
        removed = break_all_squares(n)
        print(f"Test n = {n}")
        print(f"Removed {len(removed)} toothpicks: {removed}")
        draw_board(n, removed)
        print("Valid:", "YES" if is_valid(n, removed) else "NO")
        print()