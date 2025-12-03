import numpy as np

# If you ignored DC in the forward transform, inverse transform WILL NOT WORK!
def inverse_transform(positions, meta, t_index=-1):
    """
    Inverse Orbit → Fourier → Signal → Text
    """

    N = meta["N"]
    radius_scale = meta["radius_scale"]
    gamma = meta["gamma"]

    t_index = max(0, min(t_index, positions.shape[0] - 1))
    pos_t = positions[t_index]

    # skip central star
    pos_planets = pos_t[1:N+1]

    #  Get radius and angle at time t
    r_t = np.sqrt(pos_planets[:,0]**2 + pos_planets[:,1]**2)
    theta_t = np.arctan2(pos_planets[:,1], pos_planets[:,0])

    # Invert map
    A_hat = (r_t / radius_scale) ** (1.0 / gamma)
    phi_hat = theta_t

    # Get fourier coeffs
    F_hat = A_hat * np.exp(1j * phi_hat)

    # Apply inverse fft
    signal_hat = np.fft.ifft(F_hat).real

    # Convert to ASCII
    chars = []
    for x in signal_hat:
        val = int(round(x))
        if 32 <= val <= 126:
            chars.append(chr(val))
        else:
            chars.append('?')

    return "".join(chars)
