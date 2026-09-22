#!/usr/bin/env python3
"""
MICHAEL — Pure Python implementation of the unified geometric–relativistic framework
Multiplicity, Interval, c (speed of light), ĥ (unit vector), Area, Euler limit, Angular momentum
"""

import cmath
import math
from typing import List, Tuple

# ---------------------------------------------------------------------------
# Core constants and definitions
# ---------------------------------------------------------------------------

M = 30                                  # spectroscopic multiplicity
J = (M - 1) / 2                         # → 14.5
c = 299_792_458                         # exact speed of light in vacuum (m/s)
spin_orbit_strength_scale = 1.0 / c**2  # leading-order factor ∝ 1/c²

# ---------------------------------------------------------------------------
# M — Multiplicity and magnetic quantum numbers
# ---------------------------------------------------------------------------

def magnetic_quantum_numbers(J: float) -> List[float]:
    """Return the 2J+1 distinct eigenvalues m_J from -J to +J."""
    return [J - k for k in range(int(2 * J) + 1)]

mJ_values = magnetic_quantum_numbers(J)
assert len(mJ_values) == M
assert mJ_values[0] == -J and mJ_values[-1] == J

print("=" * 70)
print("M — Multiplicity")
print(f"M = 2J + 1 = {M}  →  J = {J}")
print(f"m_J eigenvalues: {mJ_values[0]} … {mJ_values[-1]}")
print()

# ---------------------------------------------------------------------------
# I & E — Interval I=[0,1] mapped by Euler’s formula / sequential limit
# ---------------------------------------------------------------------------

def euler_sequential(theta: float, n: int) -> complex:
    """(1 + iθ/n)^n  →  e^{iθ} as n → ∞"""
    return (1 + 1j * theta / n) ** n

def unit_circle_point(t: float) -> complex:
    """z(t) = exp(i 2π t) for t ∈ [0,1]  (one full counterclockwise revolution)"""
    return cmath.exp(1j * 2 * math.pi * t)

print("I & E — Counterclockwise rotation on I = [0,1]")
print("z(t) = exp(i 2π t)")
for t in (0.0, 0.25, 0.5, 0.75, 1.0):
    z = unit_circle_point(t)
    print(f"  t = {t:4.2f}  →  z = {z.real:+.6f} {z.imag:+.6f}i   |z| = {abs(z):.10f}")
print()

print("Euler sequential limit converging to e^{i π/2} = i")
theta = math.pi / 2
for n in (1, 2, 4, 8, 16, 32, 64, 128, 256):
    approx = euler_sequential(theta, n)
    print(f"  n = {n:3d}  →  {approx.real:+.8f} {approx.imag:+.8f}i   |z| = {abs(approx):.10f}")
print()

# ---------------------------------------------------------------------------
# H — Unit vector
# ---------------------------------------------------------------------------

def unit_vector(h: complex) -> complex:
    """ĥ = h / ||h||   (length fixed at 1)"""
    norm = abs(h)
    if norm == 0:
        raise ValueError("Zero vector cannot be normalized")
    return h / norm

print("H — Unit vector ĥ = h / ||h||")
examples = [3 + 4j, 1 + 0j, 0 + 5j, -2 - 2j]
for h in examples:
    h_hat = unit_vector(h)
    print(f"  h = {h}  →  ĥ = {h_hat.real:+.6f} {h_hat.imag:+.6f}i   ||ĥ|| = {abs(h_hat):.10f}")
print()

# ---------------------------------------------------------------------------
# A — Area of the unit circle & classical angular momentum reminder
# ---------------------------------------------------------------------------

def circle_area(r: float = 1.0) -> float:
    return math.pi * r**2

print("A — Area of unit circle")
print(f"A = π r² = {circle_area():.10f}   (r = 1)")
print("Classical angular momentum reminder: L = r × p")
print()

# ---------------------------------------------------------------------------
# C & L — Relativistic scale and final partitioning statement
# ---------------------------------------------------------------------------

print("C — Relativistic scale")
print(f"c = {c} m/s")
print(f"Spin-orbit strength scales as 1/c² = {spin_orbit_strength_scale:.6e}")
print()

print("L — Projection & lifted degeneracy")
print("After spin-orbit interaction the original degeneracy is partitioned")
print("into the 30 distinct eigenvalues of J · ĥ (or J_z when ĥ = ẑ):")
print(f"  m_J ∈ {{{mJ_values[0]}, {mJ_values[1]}, …, {mJ_values[-1]}}}")
print()

# ---------------------------------------------------------------------------
# Stirling (large-N multiplicity → entropy) – uses the same e
# ---------------------------------------------------------------------------

def stirling_ln_n_factorial(n: int) -> float:
    """ln(N!) ≈ N ln N − N + ½ ln(2πN)"""
    if n <= 1:
        return 0.0
    return n * math.log(n) - n + 0.5 * math.log(2 * math.pi * n)

print("E (again) — Stirling’s approximation (macroscopic multiplicity)")
for N in (10, 100, 1000):
    print(f"  ln({N}!) ≈ {stirling_ln_n_factorial(N):.6f}")
print()

# ---------------------------------------------------------------------------
# Compact MICHAEL summary object
# ---------------------------------------------------------------------------

class MICHAEL:
    """Container that binds every letter of the acronym."""
    def __init__(self):
        self.M = M
        self.J = J
        self.mJ = mJ_values
        self.c = c
        self.I = (0.0, 1.0)
        self.strength_scale = spin_orbit_strength_scale

    def rotate(self, t: float) -> complex:
        """Continuous pure rotation of the unit vector on I=[0,1]."""
        return unit_circle_point(t)

    def normalize(self, h: complex) -> complex:
        return unit_vector(h)

    def euler_approx(self, theta: float, n: int) -> complex:
        return euler_sequential(theta, n)

    def summary(self) -> str:
        return (
            f"MICHAEL framework\n"
            f"  M = {self.M}  →  J = {self.J}\n"
            f"  m_J range = [{self.mJ[0]}, …, {self.mJ[-1]}]\n"
            f"  c = {self.c} m/s   (strength ∝ 1/c² = {self.strength_scale:.3e})\n"
            f"  Unit-circle map: z(t) = exp(i 2π t), t ∈ [0,1]\n"
            f"  Length of ĥ is invariant under pure rotation."
        )

if __name__ == "__main__":
    framework = MICHAEL()
    print("=" * 70)
    print(framework.summary())
    print("=" * 70)
    print("All geometric objects preserve length = 1.")
    print("All quantum labels remain the thirty eigenvalues of the projection")
    print("onto the same unit direction ĥ.")
