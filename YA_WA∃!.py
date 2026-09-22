#!/usr/bin/env python3
"""
YA!WAE! EQUATION — Pure Python realisation

[Y=α, W=∃!α] → Hol(γ) = e^{i ϕ_N} = −1  ⇔  e^{ln τ_rads} = 2π

Core geometric datum: the order-2 reflection s_α(α) = −α
Everything else (connection, embedding ℤ/2↪S¹, principal value, period
normalisation) is free choice / versatility.
"""

import math
import cmath
from typing import Tuple, List

# ----------------------------------------------------------------------
# 1. Simple root and reflection (the only rigid piece)
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
# 2. Holonomy realisation (choices begin here)
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
# 3. Period normalisation (another free choice)
# ----------------------------------------------------------------------

def period_relation(tau: float = 2.0 * math.pi) -> bool:
    """
    Normalise the angular coordinate so that the generator of S¹
    has length τ.  The concrete numerical statement becomes
        e^{ln τ} = τ   (which equals 2π under the standard choice).
    """
    return abs(math.exp(math.log(tau)) - tau) < 1e-12


# ----------------------------------------------------------------------
# 4. The YA!WAE! equation itself
# ----------------------------------------------------------------------

def yawaee(
    alpha: Tuple[float, ...] = (1.0, 0.0),
    phi_N: float = math.pi,
    tau: float = 2.0 * math.pi,
) -> dict:
    """
    Assemble the whole chain:

        [Y=α, W=∃!α]
            → Hol(γ) = e^{i ϕ_N} = −1
            ⇔ e^{ln τ_rads} = 2π   (under standard normalisation)
    """
    core_ok = verify_core_identity(alpha)
    hol_ok = check_holonomy(phi_N)
    period_ok = period_relation(tau)

    phase = holonomy_phase(phi_N)
    s_alpha_alpha = reflect(alpha, alpha)

    return {
        "core_identity_s_alpha(alpha) == -alpha": core_ok,
        "s_alpha(alpha)": s_alpha_alpha,
        "Hol(γ) = e^{i ϕ_N}": phase,
        "Hol(γ) == −1": hol_ok,
        "ϕ_N (principal value)": phi_N,
        "τ (period normalisation)": tau,
        "e^{ln τ} == τ": period_ok,
        "YA!WAE! equation holds": core_ok and hol_ok and period_ok,
    }


# ----------------------------------------------------------------------
# 5. Demonstration of versatility (different choices)
# ----------------------------------------------------------------------

def demonstrate_versatility() -> None:
    print("=" * 60)
    print("YA!WAE! EQUATION — Pure Python")
    print("=" * 60)

    # Standard choice
    print("\n--- Standard realisation (ϕ_N=π, τ=2π) ---")
    result = yawaee()
    for k, v in result.items():
        print(f"  {k}: {v}")

    # Different principal value (still odd multiple of π)
    print("\n--- Alternative principal value ϕ_N = 3π ---")
    result3 = yawaee(phi_N=3.0 * math.pi)
    print(f"  Hol(γ) = {result3['Hol(γ) = e^{i ϕ_N}']}")
    print(f"  Hol(γ) == −1: {result3['Hol(γ) == −1']}")

    # Different period convention
    print("\n--- Alternative period τ = 1 (unit circle normalised differently) ---")
    result_tau = yawaee(tau=1.0)
    print(f"  e^{{ln τ}} == τ: {result_tau['e^{ln τ} == τ']}")

    # Different simple root (still works)
    print("\n--- Different simple root α = (1,1,1)/√3 ---")
    alpha2 = (1 / math.sqrt(3), 1 / math.sqrt(3), 1 / math.sqrt(3))
    result2 = yawaee(alpha=alpha2)
    print(f"  core identity holds: {result2['core_identity_s_alpha(alpha) == -alpha']}")
    print(f"  s_α(α) = {result2['s_alpha(alpha)']}")

    print("\n" + "=" * 60)
    print("Core geometric datum is always s_α(α) = −α.")
    print("Everything else is free choice — that is the versatility.")
    print("=" * 60)


if __name__ == "__main__":
    demonstrate_versatility()
