import numpy as np
from gt.fourier.decomposition import (
    normalize_signal,
    compute_dft,
    compute_amplitudes_phases,
)

def test_normalize_signal_basic():
    sig = np.array([2, 4, 6])
    norm = normalize_signal(sig)
    assert np.allclose(norm, [0.0, 0.5, 1.0])

def test_normalize_signal_constant():
    sig = np.array([5, 5, 5])
    norm = normalize_signal(sig)
    assert np.all(norm == 0)

def test_compute_dft_shape():
    sig = np.random.rand(16)
    dft = compute_dft(sig)
    assert dft.shape == sig.shape

def test_amplitudes_phases_consistency():
    # simple known case: pure cosine
    N = 64
    n = np.arange(N)
    freq = 3
    sig = np.cos(2*np.pi*freq*n/N)

    dft = compute_dft(sig)
    amps, phs = compute_amplitudes_phases(dft)

    # amplitude should peak at k=freq and k=N-freq for a real cosine
    dominant = np.argmax(amps)
    assert dominant in {freq, N - freq}
