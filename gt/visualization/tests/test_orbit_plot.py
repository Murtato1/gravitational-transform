import numpy as np
from gt.visualization.orbit_plot import plot_system_snapshot, plot_orbits
import matplotlib.pyplot as plt

def test_plot_system_snapshot_runs():
    pos = np.array([[0, 0], [1, 1]])
    fig, ax = plot_system_snapshot(pos)
    assert isinstance(fig, plt.Figure)

def test_plot_orbits_runs():
    positions = np.zeros((10, 2, 2))
    fig, ax = plot_orbits(positions)
    assert isinstance(fig, plt.Figure)
