# Asteroids Game

A classic Asteroids game implementation in Python using Pygame. Navigate your spaceship through an asteroid field, destroy asteroids by shooting them, and survive as long as possible!

## Features

- **Classic Gameplay**: Faithful recreation of the classic Asteroids arcade game
- **Smooth Controls**: Responsive ship movement and rotation
- **Asteroid Spawning**: Procedurally spawned asteroid fields with varying sizes
- **Collision Detection**: Precise collision detection between player, shots, and asteroids
- **Asteroid Splitting**: Large asteroids split into smaller pieces when destroyed
- **Shooting Mechanics**: Cooldown-based shooting system with projectile physics
- **Scoring**: Points for every asteroid destroyed, with a high score that is kept between runs
- **Lives**: Three lives, with a short spell of protection after each hit
- **Rising Difficulty**: Asteroids arrive faster the longer a round lasts
- **Pause and Restart**: Pause a round, and start a new one from the game over screen

## Installation

### Prerequisites

- Python 3.13 or higher
- Pygame 2.6.1

### Setup

1. Clone the repository:
```bash
git clone https://github.com/siegblink/asteroids-game.git
cd asteroids-game
```

2. Install dependencies using uv (recommended) or pip:
```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install pygame==2.6.1
```

## How to Run

Run the game from the project root directory:

```bash
python main.py
```

Or using uv:

```bash
uv run python main.py
```

## Controls

- **A**: Rotate ship left
- **D**: Rotate ship right
- **W**: Move ship forward
- **S**: Move ship backward
- **SPACE**: Shoot projectiles
- **P**: Pause and resume
- **R**: Start a new round from the game over screen
- **ESC**: Close the game window

## Game Mechanics

### Ship Controls
- The ship rotates in place and moves in the direction it's facing
- Forward movement (W) propels the ship in the direction of the ship's nose
- Backward movement (S) moves the ship opposite to its facing direction
- Flying off one edge of the screen brings the ship back in on the opposite edge

### Asteroids
- Asteroids spawn continuously in the asteroid field
- Three different sizes of asteroids (determined by `ASTEROID_KINDS` in constants.py)
- Larger asteroids split into smaller asteroids when destroyed
- Smallest asteroids are destroyed completely when hit
- The gap between spawns shrinks from 0.8 to 0.3 seconds over the first 100 seconds of a round

### Combat
- Projectiles have a cooldown period between shots (`PLAYER_SHOOT_COOLDOWN`)
- Asteroids are destroyed when hit by projectiles
- A collision with an asteroid costs one of three lives and returns the ship to the centre, where it blinks and cannot be hit for two seconds
- The game ends when the last life is lost

### Scoring

| Asteroid | Points |
| -------- | ------ |
| Large    | 20     |
| Medium   | 50     |
| Small    | 100    |

The best score is saved in a `.highscore` file next to the game and shown at the top of the screen.

## Project Structure

```
asteroids-game/
├── main.py              # Window, clock and event loop
├── game.py              # One round: sprites, score, lives, pause and game over
├── player.py            # Player ship class and controls
├── asteroid.py          # Asteroid class and splitting mechanics
├── asteroidfield.py     # Asteroid spawning system
├── shot.py             # Projectile class
├── collisions.py       # Shots hitting asteroids
├── particle.py         # Debris when an asteroid breaks
├── hud.py              # Score, lives and on-screen messages
├── highscore.py        # Loading and saving the high score
├── circleshape.py      # Base class for circular game objects
├── constants.py        # Game configuration constants
├── tests/              # Unit tests
├── pyproject.toml      # Project configuration
└── README.md          # This file
```

## Configuration

Game settings can be modified in `constants.py`:

- `SCREEN_WIDTH` and `SCREEN_HEIGHT`: Window dimensions
- `ASTEROID_SPAWN_RATE`: How often asteroids spawn at the start of a round (in seconds)
- `ASTEROID_SPAWN_RAMP` and `ASTEROID_MIN_SPAWN_RATE`: How quickly the spawning speeds up, and its limit
- `ASTEROID_SCORES`: Points for each asteroid size
- `PLAYER_LIVES`: Lives per round
- `PLAYER_RESPAWN_INVULNERABILITY`: Protection after a hit (in seconds)
- `PLAYER_SPEED`: Ship movement speed
- `PLAYER_SHOOT_SPEED`: Projectile velocity
- `PLAYER_SHOOT_COOLDOWN`: Time between shots (in seconds)

## Dependencies

- **Pygame 2.6.1**: For game graphics, input handling, and game loop management

## Development

This project uses modern Python packaging with `uv` for dependency management. The code follows object-oriented principles with sprite groups for efficient game object management.

### Tests

The game logic is covered by unit tests in `tests/`. They use the standard
library's `unittest`, so there is nothing extra to install:

```bash
python -m unittest
```

Or using uv:

```bash
uv run python -m unittest
```

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## Credits

Classic Asteroids game concept by Atari. This implementation created as a learning project for Python game development with Pygame.
