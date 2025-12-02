# Gravitational Transform

## Motivation

How can one store information for the longest possible timescale? Conventional methods—such as silicon-based memory, magnetic storage, or even inscriptions in stone—degrade within centuries to thousands of years. More speculative ideas, such as encoding information in DNA, extend this lifetime to perhaps millions of years but still fall far short of geological or cosmological timescales.

In contrast, planetary systems exhibit orbital stability over billions of years. Their long-lived dynamical patterns naturally reside in the frequency domain, suggesting that orbital motion itself could act as an ultra-long-term information archive. One could, in principle, encode data by mapping it onto the orbital parameters of a gravitational system, letting the encoded “message’’ persist as the system evolves.

Of course, this scenario is idealized. Real planetary systems evolve due to perturbations, resonances, numerical instabilities, and long-term chaotic behavior. A central question then emerges: if information is encoded into the initial orbital configuration, how does the message transform as the gravitational system evolves?

### The Gravitational Transform

The Gravitational transform (GT) is a transform that takes in arbitrary data (in this implementation, this is strings) and computes a mapping between this data and orbital parameters. This mapping is done through using a Fourier transform as well as Newtonian physics and Kepler's laws. The system is then run with an N-body simulator and integrated over a specified time frame. Afterwards, we can obtain an evolved 'echo' of the original data. 

# Process

## 1. Fourier Decomposition
Given a discrete signal $f[n]$, we compute its discrete Fourier transform:

$$
\hat{f}_k = \sum_{n=0}^{N-1} f[n] e^{-2\pi i kn/N}
$$

For each mode $k$, define:

$$
A_k = |\hat{f}_k|, \qquad 
\phi_k = \arg(\hat{f}_k)
$$


## 2. Spectral mapping
Each Fourier mode becomes a planet. We use:

### **Amplitude to Orbital Radius**
$$
r_k = s_r \, A_k^\gamma, \qquad 0.5 \le \gamma \le 0.8
$$

This is mostly done to make the inverse transform easier while also making the visualizations well spaced.

### **Phase becomes the initial angle**
$$
\theta_k = \phi_k
$$

### **Circular orbital velocity**
Each planet has a velocity:

$$
v_k = \sqrt{\frac{G M_\star}{r_k}}
$$

where $M_\star$ is a large fixed central mass.

### **Mass**
Planet masses actually don't need to encode any data, because our implementation includes a large central star of fixed position and mass.

Then each parameter is:
$$
\mathbf{r}_k(0) = 
\begin{bmatrix}
r_k \cos\theta_k \\
r_k \sin\theta_k
\end{bmatrix},
\qquad
\mathbf{v}_k(0) =
\begin{bmatrix}
- v_k \sin\theta_k \\
+ v_k \cos\theta_k
\end{bmatrix}
$$

## 3. Gravitational Simulation
The system evolves using an N-body integrator under Newton’s laws:

$$
\frac{d^2\mathbf{r}_i}{dt^2} =
G \sum_{j\ne i}
m_j \frac{\mathbf{r}_j - \mathbf{r}_i}
{|\mathbf{r}_j - \mathbf{r}_i|^3 }
$$

This produces different trajectories:

$$
\mathcal{G}(f) = \{ \mathbf{r}_k(t), \, \mathbf{v}_k(t) \}_{k=1}^N
$$

The original message evolves under these laws and this changes the content of the original information.

# Inverse Transform 

To decode at time $t$, we just need each planet's:

$$
r_k(t) = \|\mathbf{r}_k(t)\|,
\qquad
\theta_k(t) = \text{atan2}(y_k(t), x_k(t))
$$

Then invert the original mapping:

$$
\hat{A}_k(t) = \left(\frac{r_k(t)}{s_r}\right)^{1/\gamma}
$$

$$
\hat{\phi}_k(t) = \theta_k(t)
$$

The nodes are then:

$$
\hat{f}_k(t) = \hat{A}_k(t) \, e^{i\hat{\phi}_k(t)}
$$

Inverse FFT:

$$
f_t[n] = \Re\left( IFFT(\hat{f}_k(t)) \right)
$$

Then just convert back to characters! Each value is rounded to the nearest ASCII mapping:

An example of "hello world":


![Alt text](examples/hello_world_ex.png)
