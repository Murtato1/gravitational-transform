import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_fourier_orbits(positions, meta, interval=20):
    """
    Animate the gravitational Fourier orbit system.
    Compatible with the new forward_transform() output.
    """

    # Extract number of planets (skip central star)
    N = meta["N"]

    # Initial positions
    pos0 = positions[0]
    initial_planets = pos0[1:N+1]

    # Compute radii from initial frame
    radii = np.sqrt(initial_planets[:,0]**2 + initial_planets[:,1]**2)

    # Setup figure
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_aspect("equal", "box")

    # Plot circles to show initial orbit radii
    orbit_lines = []
    for r in radii:
        circ = plt.Circle((0, 0), r, color="lightgray", fill=False, linewidth=1)
        ax.add_patch(circ)
        orbit_lines.append(circ)

    # Planet markers
    scat = ax.scatter(initial_planets[:,0], initial_planets[:,1], s=25, color="blue")

    # Axes limits (dynamic)
    lim = np.max(radii) * 2.5
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

    ax.set_title("Fourier Gravitational Orbit Animation")

    # Animation update function
    def update(frame):
        pos = positions[frame, 1:N+1]  # skip star
        scat.set_offsets(pos)

        # Auto-expand axes if orbits grow
        nonlocal lim
        max_extent = np.max(np.abs(pos)) * 1.2
        if max_extent > lim:
            lim = max_extent
            ax.set_xlim(-lim, lim)
            ax.set_ylim(-lim, lim)

        return scat,

    ani = FuncAnimation(
        fig,
        update,
        frames=range(0, positions.shape[0], 3),
        interval=interval,
        blit=True
    )

    plt.show()
    return ani
