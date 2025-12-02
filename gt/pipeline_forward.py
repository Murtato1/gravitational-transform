import numpy as np
from gt.simulation.nbody import run_simulation

def forward_transform(signal, ignore_dc=False,
                      radius_scale=3.0, gamma=0.6,
                      steps=3000, dt=0.01):
    """
    Full Fourier → Orbit Transform with optional removal of the DC (0th) Fourier mode.
    """

    # Compute Fourier coefficients
    F = np.fft.fft(signal)
    A = np.abs(F)
    phi = np.angle(F)
    N_full = len(F)

    # ----------------------------------------------------
    # OPTION: IGNORE FIRST FOURIER MODE (DC)
    # ----------------------------------------------------
    if ignore_dc:
        A = A[1:]
        phi = phi[1:]
        N = N_full - 1       # number of *planets*
        offset = 1           # index shift into F
    else:
        N = N_full           # keep all modes
        offset = 0
    # ----------------------------------------------------

    # Map amplitude → radius
    radii = radius_scale * (A ** gamma)

    # Map phase → initial θ
    theta = phi.copy()

    # Central star mass (based on full spectrum!)
    # Keeping this the same avoids shifts in dynamics
    M_star = np.sum(np.abs(F)) * 30.0

    masses = np.ones(N + 1)     # +1 for central star
    masses[0] = M_star

    # Initial position and velocity arrays
    pos = np.zeros((N + 1, 2))
    vel = np.zeros((N + 1, 2))

    # Central star at origin
    pos[0] = [0, 0]
    vel[0] = [0, 0]

    # Planets
    for j in range(N):
        k = j + offset        # actual Fourier index

        r = radii[j]
        ang = theta[j]

        pos[j + 1] = [
            r * np.cos(ang),
            r * np.sin(ang)
        ]

        # circular velocity, small epsilon to avoid NaN
        v = np.sqrt(M_star / (r + 1e-9))
        vel[j + 1] = [
            -v * np.sin(ang),
            +v * np.cos(ang)
        ]

    # Run simulation
    positions = run_simulation(pos, vel, masses, steps=steps, dt=dt)

    # Store meta data for inverse transform
    meta = {
        "radius_scale": radius_scale,
        "gamma": gamma,
        "N": N,             # number of planets (after DC removal)
        "ignored_dc": ignore_dc,
        "full_N": N_full
    }

    return positions, meta
