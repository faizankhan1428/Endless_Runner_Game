# Endless Runner Game

An endless runner game built with **Python** and **Pygame**.  
This project demonstrates how to structure a complete, playable game with clean and modular code.

## Demo

<video src="Game/game.mp4" controls width="600"></video>

## Features

- **Infinite Gameplay** – Continuously scrolling background with procedurally generated obstacles for endless replayability.  
- **Player Physics** – Gravity and jump mechanics that require precise timing.  
- **Scoring System** – Live score during play, plus a locally saved high score that persists between sessions.  
- **Main Menu & Game Over Screen** – Start fresh from the menu, and view your final score with an option to restart.  
- **Visual Effects** – Particle effects when the player lands for better feedback.  
- **Modular Code** – Components like `player`, `obstacles`, and `background` are split into separate files for easier expansion.

## Getting Started

### Prerequisites

Install **Python** and the **Pygame** library:

```bash
pip install pygame
```

### Running the Game

1. Clone or download this repository.  
2. Open a terminal or command prompt.  
3. Navigate to the project folder.  
4. Run the game with:

```bash
python main.py
```

## Project Structure

```
EndlessRunner/
│-- assets/
│   └─ sprites/
│
│-- scripts/
│   ├─ background.py
│   ├─ config.py
│   ├─ obstacle.py
│   ├─ particles.py
│   └─ player.py
│
│-- Game/
│   └─ game.mp4
│
│-- main.py
│-- highscore.txt
│-- README.md
```

## Contributing

Fork the repo, make improvements, and open a pull request. Contributions are welcome!
