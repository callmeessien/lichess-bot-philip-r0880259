Put your engines and opening books here.

# Lichess Chess Bot (Minimax + Opening Book)

This project is a **Lichess bot** that plays chess online using a **simple AI engine** I built:
- **Opening book** (plays real openings at the start)
- **Minimax + Alpha-Beta pruning** (looks ahead a few moves)
- **Evaluation function** (material + piece-square tables)

It runs using the `lichess-bot` framework and a **homemade engine** (`PyBot`) that plugs into it.

---

## What you need (Requirements)

- **Python 3.9 – 3.12** recommended (Windows / macOS / Linux)
- A **Lichess account marked as a BOT account**
- A **Lichess API token** with bot permissions
- Internet connection (because it connects to lichess.org)

---

## Project structure

These are the key files that make up my engine:

- `engines/bot/material.py` — counts piece values (material score)
- `engines/bot/positions.py` — piece-square tables (positional bonuses)
- `engines/bot/evaluation.py` — combines material + positional score
- `engines/bot/minimax.py` — minimax search with alpha-beta pruning
- `engines/bot/main.py` — chooses the best move (or opening move)
- `engines/bot/opening.py` — loads and plays moves from the opening book
- `engines/bot/opening_book.json` — the opening database (FEN -> move)

Integration with lichess-bot happens in:
- `homemade.py` — contains `PyBot`, which calls my engine’s `get_move()`

---

## Setup (Windows PowerShell)

### 1) Go into the project folder
```powershell
cd "C:\Users\YOURNAME\path\to\lichess-bot"
```

### 2) Create + activate a virtual environment
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3) Install dependencies
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

## Configure Lichess (config.yml)

You must have a config.yml in the project root.

Typical workflow:
- Copy the template (if your repo includes it):
```powershell
copy config.yml.default config.yml
```

Build the Opening Book

If your repo includes the script, you can generate/update the opening book like this:
```powershell
python .\engines\bot\scripts\opening_book.py
```

## Run the bot (connects to lichess.org)

Start the bot:
```powershell
python lichess-bot.py
```

You should see logs like:

- “Welcome <botname>!”
- “You’re now connected… awaiting challenges.”

## How to play against it

### Option A: Challenge it from your main Lichess account
1. Open your bot profile on Lichess (example: https://lichess.org/@/YOUR_BOT_NAME)
2. Click Challenge
3. Choose time control (Blitz is usually accepted; correspondence may be declined depending on config)
4. Start the game

### Option B: Bot vs bot
If you have another bot account, challenge your bot the same way.