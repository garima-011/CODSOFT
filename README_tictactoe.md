# Task 2 - Tic-Tac-Toe AI (Terminal Version)

A terminal-based Tic-Tac-Toe game built for the CodSoft Artificial Intelligence Internship.
The AI uses the **Minimax algorithm** to play optimally — it is completely unbeatable.
The best outcome a human can achieve is a draw.

## How to run
```bash
python tictactoe.py
```
No external libraries needed — pure Python!

## How to play
- You are **X**, AI is **O**
- Board positions are numbered 1-9:
```
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```
- Type a number (1-9) and press Enter to make your move
- AI responds instantly
- Best you can do is a **Draw** — the AI never loses!

## Example
```
Your move (1-9): 5
AI is thinking...
AI played at position 1

 O | 2 | 3
-----------
 4 | X | 6
-----------
 7 | 8 | 9
```

## Algorithm: Minimax
Minimax is a backtracking algorithm used in game theory. It explores all
possible future moves and picks the one that maximises the AI's chance of
winning. For a 3x3 board the full search completes instantly.

---
Built as part of the **#codsoft** Artificial Intelligence Internship.
