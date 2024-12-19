# Nim Game Solver and Simulator

This repository provides a Python implementation of the **Nim game**, a classic two-player mathematical strategy game that has been extensively studied in game theory. The code includes a solver for optimal moves and an interactive simulator where you can play against a machine opponent.

---

## What is Nim?

Nim is a **deterministic, impartial, zero-sum game** played by two players who take turns removing objects from distinct heaps. Each move follows these rules:

1. A player chooses a single heap and removes one or more objects from it.
2. Depending on the variation:
   - **Normal play**: The player who takes the last object wins.
   - **Misère play**: The player who takes the last object loses.

### Key Characteristics of Nim

1. **Perfect Information**: Both players have complete knowledge of the game's state at all times. There are no hidden elements or random events.
2. **Deterministic**: Each move leads to a predictable outcome, entirely determined by the players' decisions.
3. **Finite Structure**: The game always ends in a finite number of moves.
4. **Impartiality**: The available moves depend solely on the current state of the game, not on which player is making the move. Both players always have the same set of options.
5. **Zero-Sum**: The victory of one player corresponds directly to the loss of the other, with no possibility of a draw.

---

## Game Theory and Nim

### Zermelo’s Theorem in Nim

Nim satisfies the conditions of **Zermelo's Theorem**, which applies to finite, deterministic, two-player games with perfect information. The theorem guarantees that:
- One of the players always has a strategy to force a win.
- In games like Nim, where draws are impossible, perfect play ensures that one player will always emerge victorious.

In practical terms, Zermelo's Theorem implies that in Nim:
- The player starting from a **winning position** can always secure a win with perfect play.
- Conversely, if the starting position is a **losing position**, the opponent can force the win.

---

### Winning Strategies in Nim

The key to determining the outcome of Nim lies in calculating the **nim-sum**, which is the XOR operation applied to the sizes of all heaps. The winning strategy can be summarized as follows:

- If the **nim-sum is 0** at the start of a player's turn, that player is in a losing position. The opponent can force a win with optimal moves.
- If the **nim-sum is not 0**, the player can make a move to leave the opponent in a losing position by ensuring the resulting nim-sum becomes 0.

#### Example

For heaps of size `4`, `5`, and `7`:
- Binary representation: `4 (100), 5 (101), 7 (111)`
- Nim-sum: `100 ⊕ 101 ⊕ 111 = 010` (Decimal: 2)

The optimal move is to reduce one heap so the resulting nim-sum is `0`, putting the opponent at a disadvantage.

---

### Sprague-Grundy Theorem

The **Sprague-Grundy Theorem** generalizes Nim by showing that every impartial game can be reduced to an equivalent Nim configuration. This means:
- The same mathematical approach used to solve Nim can be applied to more complex games.
- By analyzing the nim-sum, players can determine the winning strategy in any impartial game.

---

## Features of This Repository

1. **Solver**: Calculates optimal moves for any given Nim configuration.
2. **Simulator**: Play Nim interactively against a machine that uses optimal strategies.
3. **Configurable Input**: Supports various initial heap configurations.

---

## Running the Game

### Requirements

- Python 3.6 or higher.

### Steps to Play

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/nim-game.git
   cd nim-game
   ```

2. Run the game:
   ```bash
   python nim_game.py
   ```

3. Follow the prompts to input the initial heap sizes and take turns playing against the machine.

### Example Interaction

```plaintext
LET'S PLAY NIM :)
Enter the sizes of the 4 heaps, separated by spaces: 4 5 6 7

Current heap sizes:
Heap 1: 4
Heap 2: 5
Heap 3: 6
Heap 4: 7

The machine removes 6 coins from heap 4.

Your turn. Enter the number of the heap (1-4) you want to take coins from: 3
Enter the number of coins to remove from heap 3 (1 to 6): 3

You removed 3 coins from heap 3.
```

---

## References

- [Wikipedia: Nim](https://en.wikipedia.org/wiki/Nim)

---