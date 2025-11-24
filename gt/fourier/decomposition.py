import numpy as np

def normalize_signal(signal: np.ndarray) -> np.ndarray:
    """
    Normalize a 1D input signal to the interval [0, 1].
    """
    signal = np.asarray(signal, dtype=float)
    min_val = np.min(signal)
    max_val = np.max(signal)
    if max_val == min_val:
        return np.zeros_like(signal)
    return (signal - min_val) / (max_val - min_val)


def compute_dft(signal: np.ndarray) -> np.ndarray:
    """
    Compute the discrete Fourier transform of a real-valued signal using numpy.
    Returns complex-valued coefficients for all k modes.
    """
    signal = np.asarray(signal, dtype=float)
    return np.fft.fft(signal)


def compute_amplitudes_phases(dft_coeffs: np.ndarray):
    """
    Given complex DFT coefficients, return:
        amplitudes = |c_k|
        phases = arg(c_k)
    """
    dft_coeffs = np.asarray(dft_coeffs, dtype=complex)
    amplitudes = np.abs(dft_coeffs)
    phases = np.angle(dft_coeffs)
    return amplitudes, phases
