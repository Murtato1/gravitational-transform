import numpy as np

def reconstruct_signal(times, masses, omegas, phases):
    """
    Reconstruct 1D time signal using:
        f(t) = Σ m_i * cos(ω_i t + φ_i)
    """
    times = np.asarray(times, dtype=float)
    masses = np.asarray(masses)
    omegas = np.asarray(omegas)
    phases = np.asarray(phases)

    result = np.zeros_like(times, dtype=float)
    for m, w, p in zip(masses, omegas, phases):
        result += m * np.cos(w * times + p)

    return result
