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

def calculate_total_energy(pos, vel, masses, G = 1.0):
    """Calculates the total mechanical energy (T + V) of the system."""
    # Kinetic Energy: T = 0.5 * m * v^2.
    v_sq = np.sum(vel ** 2, axis = 1)
    kinetic = 0.5 * np.sum(masses * v_sq)

    # Potential Energy: V = -G * m1 * m2 / r.
    potential = 0.0
    n = len(masses)
    for i in range(n):
        for j in range(i + 1, n):
            r_vec = pos[i] - pos[j]
            r = np.linalg.norm(r_vec)
            if r > 1e-9:
                potential -= G * masses[i] * masses[j] / r
    
    return kinetic + potential

def test_energy_conservation():
    """
    Verifies that the integrator conserves energy.
    Sets up a 2-body system and asserts that energy drift is minimal.
    """

    pos = np.array([[0.0, 0.0], [10.0, 0.0]], dtype=float)
    masses = np.array([100.0, 1.0])
    
    v_circ = np.sqrt(10.0)
    vel = np.array([[0.0, 0.0], [0.0, v_circ]], dtype=float)

    E_initial = calculate_total_energy(pos, vel, masses, G=1.0)

    dt = 0.01
    steps = 1000
    
    current_pos = pos.copy()
    current_vel = vel.copy()
    
    for _ in range(steps):
        current_pos, current_vel, _ = step_verlet(current_pos, current_vel, masses, dt=dt)

    E_final = calculate_total_energy(current_pos, current_vel, masses, G=1.0)

    energy_drift = abs(E_final - E_initial) / abs(E_initial)
    assert energy_drift < 1e-3, f"Energy conservation failed. Drift: {energy_drift:.2%}"