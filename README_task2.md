# Task 2 - Tic-Tac-Toe AI

A GUI-based Tic-Tac-Toe game built for the CodSoft Artificial Intelligence Internship.
The AI uses the **Minimax algorithm** to play optimally — it is unbeatable. The best
outcome a human can achieve is a draw.

## Features
- Beautiful dark-themed GUI built with Python Tkinter
- Unbeatable AI using the Minimax algorithm
- Colour-coded moves (✕ in red-pink, ○ in mint-green)
- Winning cells highlighted in gold
- Live scoreboard tracking wins, losses, and draws
- New Game button to restart anytime

## How to run
```bash
python tictactoe.py
```
No external libraries needed — only Python's built-in `tkinter`.

## How to play
- You are **✕** (red-pink), AI is **○** (mint-green)
- Click any empty cell to make your move
- AI responds instantly using Minimax
- Best you can do is a **Draw** — the AI never loses!

## Algorithm: Minimax
Minimax is a backtracking algorithm used in game theory. It explores all possible
future moves and picks the one that maximises the AI's chance of winning (or
minimises the human's). With Alpha-Beta pruning it can be made faster, but for a
3×3 board the full search is instant.

---
Built as part of the **#codsoft** Artificial Intelligence Internship.
