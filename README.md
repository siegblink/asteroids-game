# Asteroids Game

A classic Asteroids game implementation in Python using Pygame. Navigate your spaceship through an asteroid field, destroy asteroids by shooting them, and survive as long as possible!

## Features

- **Classic Gameplay**: Faithful recreation of the classic Asteroids arcade game
- **Smooth Controls**: Responsive ship movement and rotation
- **Asteroid Spawning**: Procedurally spawned asteroid fields with varying sizes
- **Collision Detection**: Precise collision detection between player, shots, and asteroids
- **Asteroid Splitting**: Large asteroids split into smaller pieces when destroyed
- **Shooting Mechanics**: Cooldown-based shooting system with projectile physics
- **Game Over**: Collision detection ends the game when hitting asteroids

## Installation

### Prerequisites

- Python 3.13 or higher
- Pygame 2.6.1

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd asteroids
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
- **ESC/Quit**: Close the game window

## Game Mechanics

### Ship Controls
- The ship rotates in place and moves in the direction it's facing
- Forward movement (W) propels the ship in the direction of the ship's nose
- Backward movement (S) moves the ship opposite to its facing direction

### Asteroids
- Asteroids spawn continuously in the asteroid field
- Three different sizes of asteroids (determined by `ASTEROID_KINDS` in constants.py)
- Larger asteroids split into smaller asteroids when destroyed
- Smallest asteroids are destroyed completely when hit

### Combat
- Projectiles have a cooldown period between shots (`PLAYER_SHOOT_COOLDOWN`)
- Asteroids are destroyed when hit by projectiles
- Game ends when the ship collides with an asteroid

## Project Structure

```
asteroids/
├── main.py              # Main game loop and initialization
├── player.py            # Player ship class and controls
├── asteroid.py          # Asteroid class and splitting mechanics
├── asteroidfield.py     # Asteroid spawning system
├── shot.py             # Projectile class
├── circleshape.py      # Base class for circular game objects
├── constants.py        # Game configuration constants
├── pyproject.toml      # Project configuration
└── README.md          # This file
```

## Configuration

Game settings can be modified in `constants.py`:

- `SCREEN_WIDTH` and `SCREEN_HEIGHT`: Window dimensions
- `ASTEROID_SPAWN_RATE`: How often asteroids spawn (in seconds)
- `PLAYER_SPEED`: Ship movement speed
- `PLAYER_SHOOT_SPEED`: Projectile velocity
- `PLAYER_SHOOT_COOLDOWN`: Time between shots (in seconds)

## Dependencies

- **Pygame 2.6.1**: For game graphics, input handling, and game loop management

## Development

This project uses modern Python packaging with `uv` for dependency management. The code follows object-oriented principles with sprite groups for efficient game object management.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## Credits

Classic Asteroids game concept by Atari. This implementation created as a learning project for Python game development with Pygame.
