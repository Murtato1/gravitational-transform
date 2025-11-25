import numpy as np
import matplotlib.pyplot as plt
from gt.simulation.nbody import run_simulation

def minimal_circular_orbit():
    """
    Test of confugration with no transform and just 1 body
    """
    G = 1.0
    M = 100.0  # central star
    m = 1.0    # orbiting body

    masses = np.array([M, m])

    # central star at origin
    pos0 = np.array([
        [0.0, 0.0],
        [5.0, 0.0]      # orbiting body at r=5
    ])

    # required circular velocity
    r = 5.0
    v = np.sqrt(G * M / r)

    vel0 = np.array([
        [0.0, 0.0],      # central star doesn't move
        [0.0, v]         # tangential velocity
    ])

    positions = run_simulation(pos0, vel0, masses, dt=0.01, steps=5000)

    fig, ax = plt.subplots(figsize=(6,6))
    traj = positions[:,1,:]
    ax.plot(traj[:,0], traj[:,1])
    ax.scatter([0],[0],s=50,color='orange')
    ax.set_aspect('equal','box')
    ax.set_title("Circular Orbit Test")
    plt.show()

def minimal_multi_orbit():
    """
    Test of confugration with no transform and multiple bodies
    """
    G = 1.0
    M = 200.0
    masses = [M]

    radii = [3, 5, 8, 12]
    phases = [0, 0, 0, 0]

    for r in radii:
        m = 1.0
        masses.append(m)

    masses = np.array(masses)

    # positions
    pos = [[0,0]]
    vel = [[0,0]]

    for r in radii:
        pos.append([r, 0])
        v = np.sqrt(G * M / r)
        vel.append([0, v])

    pos = np.array(pos)
    vel = np.array(vel)

    positions = run_simulation(pos, vel, masses, dt=0.01, steps=5000)

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(6,6))

    for i in range(1,len(radii)+1):
        traj = positions[:,i,:]
        ax.plot(traj[:,0], traj[:,1])

    ax.scatter([0],[0],s=50,color='orange')
    ax.set_aspect('equal','box')
    plt.show()

