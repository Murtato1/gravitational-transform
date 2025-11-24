import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_orbits(positions_over_time, interval=30, point_size=20):
    """
    Create a matplotlib animation object for the orbits.
    positions_over_time: (T, N, 2)
    """
    positions_over_time = np.asarray(positions_over_time)
    T, N, _ = positions_over_time.shape

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Orbits Animation")

    # Set axis bounds dynamically
    all_pos = positions_over_time.reshape(-1, 2)
    lim = np.max(np.abs(all_pos)) * 1.2
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

    scat = ax.scatter([], [], s=point_size)

    def update(frame):
        pos = positions_over_time[frame]
        scat.set_offsets(pos)
        return scat,

    anim = FuncAnimation(fig, update, frames=T, interval=interval, blit=True)
    return fig, anim
