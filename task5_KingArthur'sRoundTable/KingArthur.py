def seat_knights(n, friends):
    FULL = (1 << n) - 1          # bitmask with all n knights seated

    # dp[mask][v] = True if knights in 'mask' can sit in a row from 0 to v
    dp = [[False] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]
    dp[1][0] = True              # only knight 0 seated

    # Step 1: fill the table
    for mask in range(1, FULL + 1):
        if not (mask & 1):       # knight 0 must always be seated
            continue
        for v in range(n):
            if not dp[mask][v]:
                continue
            for u in range(n):
                already_seated = mask & (1 << u)
                if already_seated or not friends[v][u]:
                    continue
                new_mask = mask | (1 << u)
                if not dp[new_mask][u]:
                    dp[new_mask][u] = True
                    parent[new_mask][u] = v

    # Step 2: close the circle
    last = -1
    for v in range(1, n):
        if dp[FULL][v] and friends[v][0]:
            last = v
            break
    if last == -1:
        return []

    # Step 3: walk back through parent
    seating = []
    mask, v = FULL, last
    while v != -1:
        seating.append(v)
        p = parent[mask][v]
        mask = mask & ~(1 << v)  # remove v from the set
        v = p
    seating.reverse()
    return seating


# ---------- helpers & tests ----------
def build_friends(n, enemies):
    f = [[True] * n for _ in range(n)]
    for i in range(n):
        f[i][i] = False
    for a, b in enemies:
        f[a][b] = f[b][a] = False
    return f


def is_valid(seating, f):
    n = len(seating)
    if n == 0:
        return False
    for i in range(n):
        if not f[seating[i]][seating[(i + 1) % n]]:
            return False
    return True


def run_test(test_id, n, enemies):
    f = build_friends(n, enemies)
    seating = seat_knights(n, f)
    print(f"Test {test_id} (n = {n})")
    print("Enemies:", enemies)
    print("Seating:", seating)
    print("Valid:", "YES" if is_valid(seating, f) else "NO")
    print()


if __name__ == "__main__":
    run_test(1, 4, [(0, 2), (1, 3)])
    run_test(2, 5, [(0, 1), (2, 3)])
    run_test(3, 8, [(0, 1), (2, 3), (4, 5), (6, 7), (0, 2), (1, 3)])
