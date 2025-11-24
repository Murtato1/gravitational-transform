import numpy as np
from gt.simulation.nbody import compute_accelerations, step_verlet, run_simulation

def test_compute_accelerations_symmetry():
    pos = np.array([[0, 0], [1, 0]], dtype=float)
    masses = np.array([1.0, 1.0])

    acc = compute_accelerations(pos, masses, G=1.0)

    # gravitational symmetry: opposite accelerations
    assert np.allclose(acc[0], -acc[1])

def test_step_verlet_shapes():
    pos = np.array([[0, 0], [1, 0]], dtype=float)
    vel = np.array([[0, 0], [0, 0]], dtype=float)
    masses = np.array([1.0, 1.0])

    pos2, vel2, _ = step_verlet(pos, vel, masses, dt=0.01)
    assert pos2.shape == (2, 2)
    assert vel2.shape == (2, 2)

def test_run_simulation_steps():
    pos = np.array([[0, 0], [1, 0]], dtype=float)
    vel = np.array([[0, 0], [0, 0]], dtype=float)
    masses = np.array([1.0, 1.0])

    out = run_simulation(pos, vel, masses, dt=0.01, steps=5)
    assert out.shape == (5, 2, 2)
