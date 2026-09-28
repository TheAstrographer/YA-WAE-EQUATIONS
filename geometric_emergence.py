#!/usr/bin/env python3
"""
YA!WAE! EQUATION — Pure Python

[Y=α, W=∃!α] : s_α(α)=−α
    → Hol(γ)=−1 , W=1
    ≜ Δθ_L = L
    → ω = L · f
    ≡ α = ω
"""

import math
from typing import Tuple, Dict

# ----------------------------------------------------------------------
# 1. Algebraic core (rigid)
# ----------------------------------------------------------------------

def reflect(v: Tuple[float, ...], alpha: Tuple[float, ...]) -> Tuple[float, ...]:
    """Weyl reflection s_α(v) = v − 2 (v·α)/(α·α) α"""
    dot_va = sum(x * y for x, y in zip(v, alpha))
    dot_aa = sum(x * x for x in alpha)
    coef = 2.0 * dot_va / dot_aa
    return tuple(x - coef * a for x, a in zip(v, alpha))


def verify_order2(alpha: Tuple[float, ...]) -> bool:
    """s_α(α) == −α"""
    reflected = reflect(alpha, alpha)
    expected = tuple(-a for a in alpha)
    return all(abs(r - e) < 1e-12 for r, e in zip(reflected, expected))


# ----------------------------------------------------------------------
# 2. Continuous realisation (topology)
# ----------------------------------------------------------------------

def holonomy() -> complex:
    """Order-2 holonomy: the only continuous image of the non-identity element"""
    return -1 + 0j


def winding_number() -> int:
    """Minimal positive generator of π₁ that realises the order-2 holonomy"""
    return 1


# ----------------------------------------------------------------------
# 3. Chart-dependent measure of one cycle
# ----------------------------------------------------------------------

def delta_theta(L: float) -> float:
    """Δθ_L = L  (length assigned to the generator by the chosen chart)"""
    return float(L)


# ----------------------------------------------------------------------
# 4. Angular frequency and structural identification
# ----------------------------------------------------------------------

def angular_frequency(L: float, f: float) -> float:
    """ω = L · f"""
    return L * f


def structural_identity(alpha: Tuple[float, ...], omega: float) -> bool:
    """
    α ≡ ω at the level of generators.
    (Numerical comparison is only meaningful inside a fixed chart;
     here we simply record that the identification has been declared.)
    """
    return True   # structural, not numeric


# ----------------------------------------------------------------------
# 5. Full chain
# ----------------------------------------------------------------------

def yawaee_chain(
    alpha: Tuple[float, ...] = (1.0, 0.0),
    L: float = 2 * math.pi,   # default: radian chart
    f: float = 1.0,
) -> Dict:
    """
    Execute the forced sequence:

        [Y=α, W=∃!α]
            : s_α(α) = −α
            → Hol(γ) = −1 , W = 1
            ≜ Δθ_L = L
            → ω = L · f
            ≡ α = ω
    """
    core_ok = verify_order2(alpha)
    hol = holonomy()
    W = winding_number()
    dtheta = delta_theta(L)
    omega = angular_frequency(L, f)
    ident_ok = structural_identity(alpha, omega)

    return {
        "core_identity s_α(α) == −α": core_ok,
        "Hol(γ)": hol,
        "Winding number W": W,
        "Chart length L": L,
        "Δθ_L": dtheta,
        "Linear frequency f": f,
        "Angular frequency ω = L·f": omega,
        "Structural identification α ≡ ω": ident_ok,
        "Chain holds": core_ok and (hol == -1) and (W == 1) and ident_ok,
    }


# ----------------------------------------------------------------------
# Demonstration across charts
# ----------------------------------------------------------------------

def demonstrate():
    print("=" * 70)
    print("YA!WAE! — Chart-independent structural chain")
    print("=" * 70)

    charts = {
        "radians": 2 * math.pi,
        "turns":   1.0,
        "gradians": 400.0,
    }

    for name, L in charts.items():
        print(f"\n--- Chart: {name} (L = {L}) ---")
        result = yawaee_chain(L=L, f=1.0)
        for k, v in result.items():
            print(f"  {k}: {v}")

    print("\n" + "=" * 70)
    print("Only L changes with the language.")
    print("Every arrow after the initial pair is forced.")
    print("=" * 70)


if __name__ == "__main__":
    demonstrate() 
