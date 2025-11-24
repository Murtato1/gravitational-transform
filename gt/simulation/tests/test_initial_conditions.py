import numpy as np
from gt.simulation.initial_conditions import init_positions, init_velocities

def test_init_positions():
    radii = np.array([1.0])
    phases = np.array([0.0])
    pos = init_positions(radii, phases)
    assert pos.shape == (1, 2)
    assert np.allclose(pos, [[1.0, 0.0]])

def test_init_velocities():
    radii = np.array([1.0])
    omegas = np.array([2.0])
    phases = np.array([0.0])
    vel = init_velocities(radii, omegas, phases)
    assert vel.shape == (1, 2)
    assert np.allclose(vel, [[0.0, 2.0]])
