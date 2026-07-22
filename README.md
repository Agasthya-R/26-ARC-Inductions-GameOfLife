# ARC Game of Life Simulator — Induction Task

Welcome to the induction program for our club. This repository will guide you through the Game of Life task, helping you get started with basic Python scripting, algorithms, and terminal interfaces.

Your objective is to write the core simulation rules inside `src/solver.py` to correctly evolve a 2D grid based on Conway's Game of Life.

---

## Contents
1. [How to Submit Your Work](#how-to-submit-your-work)
2. [Prerequisites](#prerequisites)
3. [Your Task](#your-task)
4. [The Rules of Life](#the-rules-of-life)
5. [Installation & Setup](#installation--setup)
6. [The Heatmap UI](#the-heatmap-ui)
7. [Seed Configuration](#seed-configuration)
8. [Troubleshooting](#troubleshooting)

---

## How to Submit Your Work
1. **Fork this repository** into your own GitHub account.
2. Clone **your forked repository** to your local machine.
3. Complete the task by writing your solver logic inside `src/solver.py`.
4. Run `git add .` followed by `git commit -m <PR Title>` to commit your changes.
5. Run `git push` to push your changes to GitHub.
6. Submit a **Pull Request (PR)** to the main repository.
   * **PR Title format:** `NAME [ID_NUMBER]` (Example: `Archisman Das [2026B3PS0478H]`).
   * **PR Description format:** Must include your Full Name, ID Number, and Institute Email.
7. Wait for review and feedback!

---

## Prerequisites

You are not expected to have any complex frameworks installed on your machine. Everything runs using standard Python. Before starting, please ensure you have the following installed:
* **Python 3.6 or higher**
* Basic knowledge of the terminal.

---

## Your Task
1. **Task 1: `count_neighbors`:** Open `src/solver.py`. Write the logic to check the 8 surrounding cells of a given coordinate and return the total number of alive neighbors. Watch out for the edges of the grid!
2. **Task 2: `compute_next_generation`:** In the same file, use the rules of life and your new `count_neighbors` function to generate and return a brand-new grid representing the next state of the board. **You only need to edit this single file—do not modify the simulator engine or any other files.**

---

## The Rules of Life

The game takes place on a 2D grid. Every cell interacts with its eight neighbors (horizontal, vertical, and diagonal). At each step in time, the following transitions occur:

1. **Underpopulation:** Any live cell with fewer than two live neighbors dies.
2. **Survival:** Any live cell with two or three live neighbors lives on to the next generation.
3. **Overpopulation:** Any live cell with more than three live neighbors dies.
4. **Reproduction:** Any dead cell with exactly three live neighbors becomes a live cell.

---

## Installation & Setup

**Clone the Repository:**
Make sure you are cloning your own fork.
```bash
git clone <your-fork-url>
cd 26-ARC-Inductions-GameOfLife
```

**Run the Simulator:**
Open a terminal window on your host machine, navigate into the `src/` directory, and execute the engine:
```bash
cd src
python engine.py
```
*(Depending on your system, you may need to use `python3 engine.py`)*

---

## The Heatmap UI

We have built a dynamic UI in the engine that reacts to your code! Inside `src/solver.py`, the `count_neighbors` function is used to power the terminal visuals. As soon as you implement this function correctly, the simulation will light up with a vibrant thermal heatmap:
* **0-1 Neighbors:** Deep Blue (Lonely)
* **2 Neighbors:** Bright Green (Stable)
* **3 Neighbors:** Cyan (Reproducing)
* **4+ Neighbors:** Neon Red (Overcrowded)

---

## Seed Configuration

By default, the simulator loads a random map so you can immediately see chaos unfold. However, when building your logic, it is easier to test against known shapes!

Open `src/engine.py` and change the configuration at the bottom of the file in the `main()` function:
```python
# Options: 'random', 'glider', 'blinker', 'pulsar'
SEED_TYPE = 'blinker'
```
*Tip: A `blinker` should oscillate back and forth forever if your rules are implemented perfectly.*

---

## Troubleshooting

* **Script does nothing and exits instantly:** Ensure you have saved your code in your text editor. If the Python files are empty on your disk, the interpreter will exit immediately without throwing errors.
* **SyntaxError in engine.py:** You are likely using an older version of Python. Ensure you are using Python 3.6+ to support f-strings. Try running `python3 engine.py`.
* **The grid leaves "ghosts" or glitches out:** This happens if you resize your terminal window while the simulation is actively rendering. Just stop the script with `Ctrl+C` and restart it, or wait for the engine to automatically self-correct on the next frame.