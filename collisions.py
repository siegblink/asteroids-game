def resolve_hits(asteroids, shots):
    """Split every asteroid that a shot has hit and return those asteroids.

    A shot is used up by the first asteroid it hits, and an asteroid is split
    once even when several shots reach it in the same frame.
    """
    hit = []

    for asteroid in asteroids:
        for shot in shots:
            if shot.alive() and asteroid.has_collided(shot):
                shot.kill()
                asteroid.split()
                hit.append(asteroid)
                break

    return hit
