import numpy as np

def map_to_masses(amplitudes: np.ndarray, k_m: float = 1.0) -> np.ndarray:
    """
    Map Fourier amplitudes to masses using m_k = k_m * amplitude.
    """
    amplitudes = np.asarray(amplitudes, dtype=float)
    return k_m * amplitudes


def map_to_radii(k_vals: np.ndarray, k_r: float = 1.0) -> np.ndarray:
    """
    Map frequency indices k to orbital radii using r_k = k_r / k.
    We skip k = 0 because that is the DC component.
    """
    k_vals = np.asarray(k_vals, dtype=float)
    radii = np.zeros_like(k_vals)

    for i, k in enumerate(k_vals):
        if k == 0:
            radii[i] = np.inf  # DC mode → infinite radius or ignored
        else:
            radii[i] = k_r / k

    return radii


def map_to_phases(phases: np.ndarray) -> np.ndarray:
    """
    Identity mapping for phases.
    """
    return np.asarray(phases, dtype=float)


def map_to_omegas(k_vals: np.ndarray, omega0: float = 1.0) -> np.ndarray:
    """
    Map frequency mode k to angular frequency ω_k = k * ω0.
    """
    k_vals = np.asarray(k_vals, dtype=float)
    return k_vals * omega0


def assemble_bodies(amplitudes, phases, k_vals, k_m=1.0, k_r=1.0, omega0=1.0):
    masses = map_to_masses(amplitudes, k_m)
    radii  = map_to_radii(k_vals, k_r)
    phi    = map_to_phases(phases)
    omegas = map_to_omegas(k_vals, omega0)

    # Drop the k=0 term (DC offset)
    mask = k_vals != 0

    return {
        "masses": masses[mask],
        "radii": radii[mask],
        "phases": phi[mask],
        "omegas": omegas[mask],
    }
