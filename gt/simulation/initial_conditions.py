import numpy as np

def init_positions(radii: np.ndarray, phases: np.ndarray) -> np.ndarray:
    """
    Create 2D initial positions assuming circular orbits:
        x = r * cos(phi)
        y = r * sin(phi)
    """
    radii = np.asarray(radii, dtype=float)
    phases = np.asarray(phases, dtype=float)
    x = radii * np.cos(phases)
    y = radii * np.sin(phases)
    return np.stack([x, y], axis=1)  # shape (N, 2)


def init_velocities(radii, masses, phi, G=1.0):
    """
    Compute correct circular orbital velocities around central star.
    radii[0] is 0 (star at center).
    masses[0] is central mass.
    """
    radii = np.asarray(radii, dtype=float)
    phi = np.asarray(phi, dtype=float)
    masses = np.asarray(masses, dtype=float)

    vel = np.zeros((len(radii), 2))

    # central mass velocity = 0
    vel[0] = [0.0, 0.0]

    M = masses[0]  # central star mass

    for i in range(1, len(radii)):
        r = radii[i]
        if r == 0:
            vel[i] = [0.0, 0.0]
            continue

        v = np.sqrt(G * M / r)

        # tangential direction
        vx = -v * np.sin(phi[i])
        vy =  v * np.cos(phi[i])
        vel[i] = [vx, vy]

    return vel
