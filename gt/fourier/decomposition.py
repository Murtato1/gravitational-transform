import numpy as np

def normalize_signal(signal: np.ndarray) -> np.ndarray:
    """
    Normalize a 1D input signal from [0, 1]
    """
    signal = np.asarray(signal, dtype=float)
    min_val = np.min(signal)
    max_val = np.max(signal)
    if max_val == min_val:
        return np.zeros_like(signal)
    return (signal - min_val) / (max_val - min_val)


def compute_dft(signal: np.ndarray) -> np.ndarray:
    """
    Compute the discrete Fourier transform of real value signal using numpy.
    Returns complex coefficients for all k modes.
    """
    signal = np.asarray(signal, dtype=float)
    return np.fft.fft(signal)


def compute_amplitudes_phases(dft_coeffs: np.ndarray):
    """
    Returns:
        amplitudes = |c_k|
        phases = arg(c_k)
    Given the DFT coefficients
    """
    dft_coeffs = np.asarray(dft_coeffs, dtype=complex)
    amplitudes = np.abs(dft_coeffs)
    phases = np.angle(dft_coeffs)
    return amplitudes, phases
