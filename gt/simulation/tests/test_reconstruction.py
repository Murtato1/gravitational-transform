import numpy as np
from gt.simulation.reconstruction import reconstruct_signal

def test_reconstruct_signal_simple():
    times = np.linspace(0, np.pi, 5)
    masses = np.array([1.0])
    omegas = np.array([1.0])
    phases = np.array([0.0])

    out = reconstruct_signal(times, masses, omegas, phases)
    expected = np.cos(times)
    assert np.allclose(out, expected)
