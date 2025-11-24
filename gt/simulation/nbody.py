import numpy as np

def compute_accelerations(positions: np.ndarray, masses: np.ndarray, G: float = 1.0):
    """
    Compute gravitational accelerations on all bodies.
    positions: shape (N, 2)
    masses: shape (N,)
    returns: accelerations shape (N, 2)
    """
    N = positions.shape[0]
    acc = np.zeros_like(positions)

    for i in range(N):
        r_i = positions[i]
        total = np.zeros(2)
        for j in range(N):
            if i == j:
                continue
            r_j = positions[j]
            diff = r_j - r_i
            dist3 = np.linalg.norm(diff)**3 + 1e-12  # avoid div-zero
            total += G * masses[j] * diff / dist3
        acc[i] = total

    return acc


def step_verlet(pos, vel, masses, dt, G=1.0):
    acc = compute_accelerations(pos, masses, G)

    pos_new = pos + vel * dt + 0.5 * acc * dt * dt
    acc_new = compute_accelerations(pos_new, masses, G)
    vel_new = vel + 0.5 * (acc + acc_new) * dt

    # ============================================
    # 🔥 FIX: keep the central mass pinned at origin
    # ============================================
    pos_new[0] = np.array([0.0, 0.0])
    vel_new[0] = np.array([0.0, 0.0])
    # ============================================

    return pos_new, vel_new, acc_new



def run_simulation(pos0, vel0, masses, dt, steps, G=1.0):
    """
    Run a full simulation.
    Returns:
        positions_over_time: shape (steps, N, 2)
    """
    pos = pos0.copy()
    vel = vel0.copy()

    N = pos0.shape[0]
    positions_over_time = np.zeros((steps, N, 2))

    for s in range(steps):
        positions_over_time[s] = pos
        pos, vel, _ = step_verlet(pos, vel, masses, dt, G)

    return positions_over_time
