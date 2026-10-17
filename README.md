# Tic-Tac-Toe

A two-player tic-tac-toe game that runs in the terminal. Players take turns placing **X** and **O** on a 3×3 board until someone wins or the board is full.

The game prompts are in Hebrew.

## Requirements

- Python 3

## How to run

From the project folder:

```bash
python tictactoc.py
```

On some systems you may need `python3` instead of `python`.

## How to play

1. Player **X** starts.
2. On your turn, enter a row and column as two numbers from `1` to `3`, separated by a space.  
   Example: `1 2` places your mark in row 1, column 2.
3. If a cell is already taken, or the input is invalid, you will be asked to try again.
4. The game ends when a player gets three in a row (horizontal, vertical, or diagonal), or when the board is full (tie).

## File

- `tictactoc.py` — game logic, board display, win/tie checks, and the main loop
