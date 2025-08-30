# Endless Runner Game

An endless runner game created with Python and the Pygame library. This project serves as a comprehensive example of a complete, playable game with a focus on clean, modular code.

## Features

-   **Infinite Gameplay:** The game features a continuously scrolling background and procedurally generated obstacles, providing endless replayability.
-   **Player Physics:** The player character has gravity and jump mechanics, requiring precise timing to navigate the obstacles.
-   **Scoring System:** A live score tracks how long you've survived, and a high score is saved locally, persisting between game sessions.
-   **Main Menu & Game Over Screen:** A main menu provides a clean start, while a game over screen displays your final score and allows you to restart the game.
-   **Visual Effects:** Particle effects are generated on the player's landing for added visual feedback.
-   **Modular Code:** The game is structured with separate files for different components (`player`, `obstacles`, `background`), making it easy to understand and expand.

## Getting Started

### Prerequisites

To run this game, you need to have **Python** and the **Pygame** library installed.

```bash
pip install pygame

How to Run
Clone this repository or download the project files.

Open your terminal or command prompt.

Navigate to the main project directory.

Run the main game file with the following command:

Bash

python main.py
Project Structure
The project is organized into logical folders to keep the codebase clean:

EndlessRunner/
|-- assets/
|   |-- sounds/
|   |-- sprites/
|
|-- scripts/
|   |-- background.py
|   |-- config.py
|   |-- obstacle.py
|   |-- particles.py
|   |-- player.py
|
|-- main.py
|-- highscore.txt
|-- README.md
How to Contribute
Feel free to fork the repository, make improvements, and submit a pull request.
