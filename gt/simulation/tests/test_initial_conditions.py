import numpy as np
from gt.simulation.initial_conditions import init_velocities

def test_gravity_velocity_magnitude():
    radii = np.array([0.0, 1.0])     # star at center, one planet
    masses = np.array([10.0, 1.0])   # central mass = 10
    phi = np.array([0.0, 0.0])       # angle = 0

    vel = init_velocities(radii, masses, phi, G=1.0)

    # expected circular v = sqrt(GM/r) = sqrt(10)
    expected_v = np.sqrt(10.0)

    # direction: vx = 0, vy = +v
    assert np.allclose(vel[1], [0.0, expected_v])

def test_velocity_direction_from_phase():
    radii  = np.array([0.0, 2.0])
    masses = np.array([5.0, 1.0])
    phi    = np.array([0.0, np.pi/2])  # 90 degrees

    vel = init_velocities(radii, masses, phi)

    # expected speed:
    v = np.sqrt(5.0 / 2.0)

    expected_vx = -v * np.sin(np.pi/2)   # = -v
    expected_vy =  v * np.cos(np.pi/2)   # = 0

    assert np.allclose(vel[1], [expected_vx, expected_vy])

def test_central_mass_at_rest():
    radii  = np.array([0.0, 3.0, 5.0])
    masses = np.array([20.0, 1.0, 2.0])
    phi    = np.zeros(3)

    vel = init_velocities(radii, masses, phi)

    assert np.allclose(vel[0], [0.0, 0.0])

def test_zero_radius_body():
    radii  = np.array([0.0, 0.0])
    masses = np.array([15.0, 1.0])
    phi    = np.array([0.0, 1.23])

    vel = init_velocities(radii, masses, phi)

    assert np.allclose(vel[1], [0.0, 0.0])
