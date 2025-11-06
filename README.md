# Gravitational Transform

## Motivation

If you wanted to store information for the longest amount of time possible, how would you do it? Computer chips will fail in centuries, etchings in stone will only last thousands, and even more creative answers like DNA encoding can only theoretically last millions. Meanwhile, planetary system orbits can be stable for billions of years, and orbital patterns can encode information in the frequency domain. So, an unrealistic but interesting answer to the posed question is to transform the desired piece of information into orbital patterns with different masses and store the information within the dynamics of the system.

The **Gravitational Transform** works by Fourier transforming arbitrary data and then converting this into a gravitational simulation.

## Process
1. **Fourier Decomposition**  
   Decompose your data into amplitudes and phases using a discrete Fourier transform (DFT).

2. **Spectral Mapping**  
   - Amplitude is mapped to object mass
   - Frequency is mapped to Orbital Radius / Angular Velocity  
   - Phase → Initial Angle

3. **Gravitational Simulation**  
   Use an n-body integrator to evolve the system under gravitational dynamics.

4. **Visualization**  
   Render the result as a real-time simulation.

## Math

Given a discrete signal $f(t)$ with period $T$, its Fourier series is
$$
f(t) = a_0 + \sum_{n=1}^{N}
       [a_n \cos(n\omega_0 t)
            + b_n \sin(n\omega_0 t)],
\qquad
\omega_0 = \frac{2\pi}{T}
$$

The amplitude and phase for each node is:


$$
A_n = \sqrt{a_n^2 + b_n^2},
\qquad
\phi_n = \tan^{-1}\!\left(\frac{b_n}{a_n}\right)
$$

Each Fourier mode, in the gravitational transform, maps to a body in a gravitational simulation:
$$
m_n = k_m A_n, \qquad
r_n = \frac{k_r}{n}, \qquad
\omega_n = n\omega_0
$$

Positions evolve according to Newton’s law of gravitation:

$$
\frac{d^2 \mathbf{r}_i}{dt^2}
  = G \sum_{j\neq i}
    m_j \frac{\mathbf{r}_j - \mathbf{r}_i}
              {|\mathbf{r}_j - \mathbf{r}_i|^3}
              $$

The **Gravitational Transform**

$$
\mathcal{G}[f(t)] =
\{\mathbf{r}_n(t),\mathbf{v}_n(t),m_n\}
$$

is a mapping from frequency space to dynamical, gravitational space.

## Example 

Let's consider the sentence "hello world" as an example:

> `"hello world"`

This sentence can be transformed into an array of normalized ascii values:

$$
f = [0.408,\ 0.396,\ 0.424,\ 0.424,\ 0.435,\ 0.125,\ 
     0.467,\ 0.435,\ 0.447,\ 0.424,\ 0.392]
$$

We can take the discrete Fourier transform of this:

$$
\hat{f}_k = \sum_{n=0}^{N-1}
  f_n\  e^{-2\pi i kn / N},
\quad N = 11.
$$

Each mode $k$ has amplitude
$|\hat{f}_k|$ and phase
$\phi_k = \arg(\hat{f}_k)$

These become orbital parameters:
<table>
  <tr>
    <th>k</th>
    <th>mₖ ∝ |f̂ₖ|</th>
    <th>rₖ ∝ 1/k</th>
    <th>ωₖ ∝ k</th>
    <th>φₖ (rad)</th>
  </tr>
  <tr><td>1</td><td>0.45</td><td>1.0</td><td>1 · ω₀</td><td>2.53</td></tr>
  <tr><td>2</td><td>0.23</td><td>0.5</td><td>2 · ω₀</td><td>3.66</td></tr>
  <tr><td>3</td><td>0.20</td><td>0.33</td><td>3 · ω₀</td><td>−1.10</td></tr>
  <tr><td>…</td><td>…</td><td>…</td><td>…</td><td>…</td></tr>
</table>


Simulating these under Newton's laws gives us a "planetary" system whose orbital interference patterns has the spectral components of “hello world”.

If we project the x-positions of all masses back over time,

$f'(t) = \sum_i m_i \cos(\omega_i t + \phi_i)$

we obtain a gravitationally evolved echo of the original phrase.