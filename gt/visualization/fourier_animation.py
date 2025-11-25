import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_fourier_orbits(positions, meta, message="", interval=20):
    """
    Animate the gravitational Fourier orbit system.
    Compatible with the new forward_transform() output.
    """

    N = meta["N"]                      
    pos0 = positions[0]
    planets0 = pos0[1:N+1]            # skip central mass

    # Extract radii from initial frame
    radii = np.linalg.norm(planets0, axis=1)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_aspect("equal", "box")
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    if message:
        ax.set_title(f"Gravitational Transform of:  '{message}'",
                     color="white", fontsize=14)

    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Central Star
    star = plt.Circle((0, 0), radii.max()*0.05,
                      color="white", zorder=5, alpha=0.9)
    ax.add_patch(star)

    orbit_lines = []
    for r in radii:
        ring = plt.Circle((0,0), r, color="gray", linewidth=0.8,
                          fill=False, alpha=0.3)
        ax.add_patch(ring)
        orbit_lines.append(ring)

    # Trails
    trail_len = 120       
    trail_x = [ [] for _ in range(N) ]
    trail_y = [ [] for _ in range(N) ]

    trail_lines = [
        ax.plot([], [], color="cyan", linewidth=1, alpha=0.6)[0]
        for _ in range(N)
    ]

    # Planet circles
    scat = ax.scatter(planets0[:,0], planets0[:,1],
                      s=30, color="cyan", edgecolor="white", linewidths=0.4)

    # Limits
    lim = radii.max() * 2.2
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

    # Main update
    def update(frame):
        nonlocal lim

        pos = positions[frame, 1:N+1]      # (N, 2)
        scat.set_offsets(pos)

        # Update trails
        for i in range(N):
            trail_x[i].append(pos[i,0])
            trail_y[i].append(pos[i,1])

            if len(trail_x[i]) > trail_len:
                trail_x[i].pop(0)
                trail_y[i].pop(0)

            trail_lines[i].set_data(trail_x[i], trail_y[i])

        # Auto zoom
        max_extent = np.max(np.abs(pos)) * 1.3
        if max_extent > lim:
            lim = max_extent
            ax.set_xlim(-lim, lim)
            ax.set_ylim(-lim, lim)

        return scat, *trail_lines

    ani = FuncAnimation(
        fig,
        update,
        frames=range(0, positions.shape[0], 2),
        interval=interval,
        blit=True
    )

    plt.show()
    return ani