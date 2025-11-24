import numpy as np
from gt.visualization.animation import animate_orbits
import matplotlib.animation as animation
import matplotlib.pyplot as plt

def test_animate_orbits_return_type():
    positions = np.zeros((20, 3, 2))
    fig, anim = animate_orbits(positions)
    assert isinstance(fig, plt.Figure)
    assert isinstance(anim, animation.FuncAnimation)
