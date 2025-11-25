import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from gt.simulation.nbody import run_simulation


def animate_circular_orbit():
    """
    Test of animation and orbit simulation without any transform data
    """
    G = 1.0
    M = 100.0
    m = 1.0

    masses = np.array([M, m])
    pos0 = np.array([[0.0, 0.0],
                     [5.0, 0.0]])

    r = 5.0
    v = np.sqrt(G * M / r)

    vel0 = np.array([[0.0, 0.0],
                     [0.0, v]])

    # run full simulation
    positions = run_simulation(pos0, vel0, masses, dt=0.01, steps=3000)

    # ---------- SETUP FIGURE ----------
    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_aspect("equal", "box")
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)
    ax.set_title("Circular Orbit Animation")

    # star + planet
    star = ax.scatter([0], [0], s=80, color='orange')
    planet = ax.scatter([], [], s=30, color='blue')
    trail, = ax.plot([], [], color='blue', linewidth=1)

    # pre-store trajectory for trail effect
    planet_traj_x = []
    planet_traj_y = []

    def update(frame):
        x, y = positions[frame, 1]

        planet.set_offsets([[x, y]])

        # add to trail
        planet_traj_x.append(x)
        planet_traj_y.append(y)
        trail.set_data(planet_traj_x, planet_traj_y)

        return planet, trail

    anim = FuncAnimation(fig, update, frames=len(positions), interval=16, blit=True)
    plt.show()
