import numpy as np
from gt.fourier.mapping import (
    map_to_masses,
    map_to_radii,
    map_to_phases,
    map_to_omegas,
    assemble_bodies,
)

def test_map_to_masses():
    amps = np.array([1, 2, 3])
    masses = map_to_masses(amps, k_m=2.0)
    assert np.allclose(masses, [2, 4, 6])

def test_map_to_radii():
    k = np.array([0, 1, 2, 4])
    radii = map_to_radii(k, k_r=10)
    # k=0 should be inf
    assert np.isinf(radii[0])
    assert radii[1] == 10
    assert radii[2] == 5
    assert radii[3] == 2.5

def test_map_to_phases():
    phases = np.array([0.1, -1.3])
    assert np.allclose(map_to_phases(phases), phases)

def test_map_to_omegas():
    k = np.array([0, 1, 2])
    omegas = map_to_omegas(k, omega0=5)
    assert np.allclose(omegas, [0, 5, 10])

def test_assemble_bodies_output():
    amps = np.array([1, 2])
    phases = np.array([0.2, 0.3])
    k_vals = np.array([1, 2])

    result = assemble_bodies(amps, phases, k_vals, k_m=2, k_r=10, omega0=1)

    assert set(result.keys()) == {"masses", "radii", "phases", "omegas"}
    assert np.allclose(result["masses"], [2, 4])
    assert np.allclose(result["radii"], [10, 5])
    assert np.allclose(result["phases"], phases)
    assert np.allclose(result["omegas"], [1, 2])
