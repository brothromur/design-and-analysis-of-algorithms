# EED461: Design and Analysis of Algorithms — Project Repository

**Course:** EED461 — Design and Analysis of Algorithms (2026/2027)  
**Institution:** Ain Shams University, Faculty of Engineering — Computer Engineering and Software Systems Program

---

## Overview

This repository contains the implementations, test cases, and supporting resources for all eight algorithmic tasks required in the EED461 group project. Each task is implemented using its **mandated algorithmic paradigm**.

---

## Tasks & Required Techniques

| # | Task | Required Technique | Function Signature |
| :- | :--- | :--- | :--- |
| 1 | **Coin Removal** | Greedy | `removeCoins(n: int, coins: char[]) -> (possible: bool, flips: int[])` |
| 2 | **Domino Tiling** | Brute Force | `tileDominoes(n: int, missing1: (row, col), missing2: (row, col)) -> (possible: bool, dominoes: (row, col)[])` ($2 \le n \le 8$) |
| 3 | **Security Switches** | Decrease and Conquer | `turnOffSwitches(n: int) -> (minMoves: int, toggles: int[])` |
| 4 | **Point Coloring** | Iterative Improvement | `colorPoints(n: int, points: (x, y)[]) -> colors: char[]` |
| 5 | **King Arthur's Round Table** | Dynamic Programming | `seatKnights(n: int, friends: bool[][]) -> seating: int[]` ($n > 2$) |
| 6 | **Killing Squares** | Dynamic Programming | `breakAllSquares(n: int) -> removedToothpicks: (row, col)[]` |
| 7 | **Poisoned Wine** | Divide and Conquer | `designWineTests(testers: int) -> (possible: bool, schedule, decoder)` |
| 8 | **Colored Tromino Tiling** | Divide and Conquer | `tileTromino(n: int, missingRow: int, missingCol: int) -> tiles: Tromino[]` ($2^n \times 2^n$, $n > 1$) |

---

## Problem Summaries

1. **Coin Removal:** Determine whether a line of heads/tails coins can be cleared by repeatedly removing a heads-up coin and flipping its original immediate neighbors, returning a valid removal sequence.
2. **Domino Tiling:** Determine whether an $n \times n$ chessboard ($2 \le n \le 8$) missing two opposite-colored squares can be tiled with non-overlapping $2 \times 1$ dominoes, returning a valid placement if one exists.
3. **Security Switches:** Turn off a row of $n$ switches (initially all on) in the minimum number of legal single-switch toggles and output the exact toggle sequence.
4. **Point Coloring:** Color $n$ distinct planar points black or white so every horizontal and vertical line containing points has equal or differing-by-one color counts.
5. **King Arthur's Round Table:** Arrange $n > 2$ knights around a circular table so no two enemies sit adjacent, given mutual friendships where each knight is friends with at least $\lceil n/2 \rceil$ knights.
6. **Killing Squares:** Find a minimum-size set of toothpicks to remove from an $n \times n$ toothpick grid so that the perimeter of every square of every size is broken.
7. **Poisoned Wine:** Determine whether 10 (and 8) testers can identify 1 poisoned barrel among 1,000 within 35 days given a 30-day symptom delay, and construct the testing schedule and decoder.
8. **Colored Tromino Tiling:** Tile a $2^n \times 2^n$ ($n > 1$) board missing one cell using non-overlapping L-shaped trominoes colored with 3 colors so no edge-adjacent trominoes share a color.[cite: 3, 4, 5]
