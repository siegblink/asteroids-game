import os

# The tests never open a window: SDL's dummy drivers stand in for the
# display and the sound card
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
