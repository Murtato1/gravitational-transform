import numpy as np
from gt.simulation.nbody import run_simulation

def forward_transform(signal, radius_scale=3.0, gamma=0.6, steps=3000, dt=0.01):
    """
    Full Fourier → Orbit Transform (Option B).
    """

    # -----------------------------------------
    # 1) Compute true Fourier coefficients
    # -----------------------------------------
    F = np.fft.fft(signal)
    A = np.abs(F)          # amplitudes
    phi = np.angle(F)      # phases
    N = len(F)

    # -----------------------------------------
    # 2) Map amplitude → radius (nonlinear)
    # -----------------------------------------
    radii = radius_scale * (A ** gamma)

    # phases → theta
    theta = phi.copy()

    # -----------------------------------------
    # 3) Generate initial orbit state
    # -----------------------------------------
    M_star = np.sum(A) * 30.0   # big central mass
    masses = np.ones(N + 1)     # 0 = star, 1..N planets
    masses[0] = M_star

    # positions
    pos = np.zeros((N + 1, 2))
    vel = np.zeros((N + 1, 2))

    # center star stays at origin
    pos[0] = [0, 0]

    # planets
    for k in range(N):
        r = radii[k]
        ang = theta[k]

        pos[k + 1] = [
            r * np.cos(ang),
            r * np.sin(ang)
        ]

        # circular velocity
        v = np.sqrt(M_star / (r + 1e-9))
        vel[k + 1] = [
            -v * np.sin(ang),
            +v * np.cos(ang)
        ]

    # -----------------------------------------
    # 4) Run simulation
    # -----------------------------------------
    positions = run_simulation(pos, vel, masses, steps=steps, dt=dt)

    # store orbit parameters for inverse
    meta = {
        "radius_scale": radius_scale,
        "gamma": gamma,
        "N": N
    }

    return positions, meta
