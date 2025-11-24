import numpy as np
import matplotlib.pyplot as plt

def plot_system_snapshot(positions, ax=None, title="Initial System", point_size=40):
    """
    Plot a single snapshot of body positions.
    positions: (N, 2)
    """
    positions = np.asarray(positions)

    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 6))
    else:
        fig = ax.figure

    ax.scatter(positions[:, 0], positions[:, 1], s=point_size)

    ax.set_aspect("equal", "box")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(title)

    return fig, ax


def plot_orbits(positions_over_time, ax=None, point_size=10):
    """
    Plot the full orbit trace for each object.
    positions_over_time: (T, N, 2)
    """
    positions_over_time = np.asarray(positions_over_time)
    T, N, _ = positions_over_time.shape

    if ax is None:
        fig, ax = plt.subplots(figsize=(7, 7))
    else:
        fig = ax.figure

    for i in range(N):
        traj = positions_over_time[:, i, :]
        ax.plot(traj[:, 0], traj[:, 1], alpha=0.7)
        ax.scatter([traj[0, 0]], [traj[0, 1]], s=point_size)

    ax.set_aspect("equal", "box")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Orbital Trajectories")

    return fig, ax
