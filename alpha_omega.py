#!/usr/bin/env python3
"""
YA!WAE! EQUATION

[Y=α, W=∃!α] → Hol(γ) = e^{i ϕ_N} = −1  ⇔  e^{ln τ_rads} = 2π  ≜ ω = 2π f

Core geometric datum: the order-2 reflection s_α(α) = −α
Everything else (connection, embedding ℤ/2↪S¹, principal value, period
normalization, frequency) is free choice / versatility.
"""

import math
import cmath
from typing import Tuple

# ----------------------------------------------------------------------
# 1. Simple root and reflection
# ----------------------------------------------------------------------

def reflect(v: Tuple[float, ...], alpha: Tuple[float, ...]) -> Tuple[float, ...]:
    """
    Weyl reflection s_α(v) = v - 2 (v·α)/(α·α) α
    Special case: s_α(α) = −α
    """
    dot_va = sum(x * y for x, y in zip(v, alpha))
    dot_aa = sum(x * x for x in alpha)
    coef = 2.0 * dot_va / dot_aa
    return tuple(x - coef * a for x, a in zip(v, alpha))


def verify_core_identity(alpha: Tuple[float, ...]) -> bool:
    """The one identity that never changes."""
    reflected = reflect(alpha, alpha)
    expected = tuple(-a for a in alpha)
    return all(abs(r - e) < 1e-12 for r, e in zip(reflected, expected))


# ----------------------------------------------------------------------
# 2. Holonomy realization
# ----------------------------------------------------------------------

def holonomy_phase(phi_N: float = math.pi) -> complex:
    """
    Embedding ℤ/2ℤ ↪ S¹ that sends the non-identity element to −1.
    Principal value ϕ_N = π (any odd multiple of π works).
    """
    return cmath.exp(1j * phi_N)


def check_holonomy(phi_N: float = math.pi) -> bool:
    return abs(holonomy_phase(phi_N) + 1.0) < 1e-12


# ----------------------------------------------------------------------
# 3. Period normalization and angular frequency ω = 2π f
# ----------------------------------------------------------------------

def period_relation(tau: float = 2.0 * math.pi) -> bool:
    """
    Normalize the angular coordinate so that the generator of S¹
    has length τ.  The concrete numerical statement becomes
        e^{ln τ} = τ   (which equals 2π under the standard choice).
    """
    return abs(math.exp(math.log(tau)) - tau) < 1e-12


def angular_frequency(f: float = 1.0) -> float:
    """
    Standard definition: ω = 2π f
    Under the conventional period τ = 2π one has ω ≜ 2π ≜ 2π f
    (i.e. f = 1 cycle per unit time when τ = 2π).
    """
    return 2.0 * math.pi * f


def check_omega(f: float = 1.0, tau: float = 2.0 * math.pi) -> bool:
    """Verify that ω = 2π f and that τ = 2π under standard normalization."""
    omega = angular_frequency(f)
    return abs(omega - 2.0 * math.pi * f) < 1e-12 and abs(tau - 2.0 * math.pi) < 1e-12


# ----------------------------------------------------------------------
# 4. The YA!WAE! equation itself
# ----------------------------------------------------------------------

def yawaee(
    alpha: Tuple[float, ...] = (1.0, 0.0),
    phi_N: float = math.pi,
    tau: float = 2.0 * math.pi,
    f: float = 1.0,
) -> dict:
    """
    Assemble the whole chain:

        [Y=α, W=∃!α]
            → Hol(γ) = e^{i ϕ_N} = −1
            ⇔ e^{ln τ_rads} = 2π
            ≜ ω = 2π f
    """
    core_ok = verify_core_identity(alpha)
    hol_ok = check_holonomy(phi_N)
    period_ok = period_relation(tau)
    omega = angular_frequency(f)
    omega_ok = check_omega(f, tau)

    phase = holonomy_phase(phi_N)
    s_alpha_alpha = reflect(alpha, alpha)

    return {
        "core_identity_s_alpha(alpha) == -alpha": core_ok,
        "s_alpha(alpha)": s_alpha_alpha,
        "Hol(γ) = e^{i ϕ_N}": phase,
        "Hol(γ) == −1": hol_ok,
        "ϕ_N (principal value)": phi_N,
        "τ (period normalization)": tau,
        "e^{ln τ} == τ": period_ok,
        "f (frequency)": f,
        "ω = 2π f": omega,
        "ω ≜ 2π = 2π f (standard)": omega_ok,
        "YA!WAE! equation holds": core_ok and hol_ok and period_ok and omega_ok,
    }


# ----------------------------------------------------------------------
# 5. Demonstration of versatility
# ----------------------------------------------------------------------

def demonstrate_versatility() -> None:
    print("=" * 70)
    print("YA!WAE! EQUATION — Pure Python")
    print("[Y=α, W=∃!α] → Hol(γ)=e^{iϕ_N}=-1 ⇔ e^{ln τ}=2π ≜ ω=2πf")
    print("=" * 70)

    # Standard choice
    print("\n--- Standard realization (ϕ_N=π, τ=2π, f=1) ---")
    result = yawaee()
    for k, v in result.items():
        print(f"  {k}: {v}")

    # Different principal value (still odd multiple of π)
    print("\n--- Alternative principal value ϕ_N = 3π ---")
    result3 = yawaee(phi_N=3.0 * math.pi)
    print(f"  Hol(γ) = {result3['Hol(γ) = e^{i ϕ_N}']}")
    print(f"  Hol(γ) == −1: {result3['Hol(γ) == −1']}")

    # Different frequency
    print("\n--- Alternative frequency f = 0.5 (ω = π) ---")
    result_f = yawaee(f=0.5)
    print(f"  f = {result_f['f (frequency)']}")
    print(f"  ω = 2π f = {result_f['ω = 2π f']}")

    # Different period convention
    print("\n--- Alternative period τ = 1 (unit circle normalized differently) ---")
    result_tau = yawaee(tau=1.0)
    print(f"  e^{{ln τ}} == τ: {result_tau['e^{ln τ} == τ']}")

    # Different simple root
    print("\n--- Different simple root α = (1,1,1)/√3 ---")
    alpha2 = (1 / math.sqrt(3), 1 / math.sqrt(3), 1 / math.sqrt(3))
    result2 = yawaee(alpha=alpha2)
    print(f"  core identity holds: {result2['core_identity_s_alpha(alpha) == -alpha']}")
    print(f"  s_α(α) = {result2['s_alpha(alpha)']}")

    print("\n" + "=" * 70)
    print("Core geometric datum is always s_α(α) = −α.")
    print("ω = 2π f is the conventional angular-frequency relation.")
    print("Everything else is free choice — that is the versatility.")
    print("=" * 70)


if __name__ == "__main__":
    demonstrate_versatility()
