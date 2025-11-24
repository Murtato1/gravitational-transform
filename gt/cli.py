import matplotlib
matplotlib.use("TkAgg")

import typer
import numpy as np

from gt.pipeline_forward import forward_transform
from gt.pipeline_inverse import inverse_transform
from gt.visualization.fourier_animation import animate_fourier_orbits

app = typer.Typer(help="Gravitational Transform CLI")


@app.command()
def text(message: str, animate: bool = False):
    """
    Forward transform + animation only.
    """
    sig = np.array([ord(c) for c in message], dtype=float)

    positions, meta = forward_transform(sig)

    if animate:
        animate_fourier_orbits(positions, meta)


@app.command()
def evolve(message: str, time: int = -1):
    """
    Forward → evolve → inverse transform (decode at specified time).
    """
    sig = np.array([ord(c) for c in message], dtype=float)

    positions, meta = forward_transform(sig)

    decoded = inverse_transform(positions, meta, t_index=time)
    print(f"Decoded at t={time}:", decoded)


def run():
    app()
