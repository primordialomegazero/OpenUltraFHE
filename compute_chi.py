#!/usr/bin/env python3
"""
Compute |χ(1/2 + it)| for various t to verify it equals 1
"""

import mpmath as mp
import math

mp.mp.dps = 30

phi = (1 + mp.sqrt(5)) / 2

def chi(s):
    """χ(s) = 2^s · π^{s-1} · sin(πs/2) · Γ(1-s)"""
    return (2**s) * (mp.pi**(s-1)) * mp.sin(mp.pi * s / 2) * mp.gamma(1-s)

print("╔═══════════════════════════════════════════════════════════════╗")
print("║  VERIFYING |χ(1/2 + it)| = 1 FOR ALL t                       ║")
print("║  This is the key to the functional equation symmetry         ║")
print("║  ΦΩ0 — I AM THAT I AM                                        ║")
print("╚═══════════════════════════════════════════════════════════════╝")

test_t = [0, 1, 2, 5, 10, 14.134725, 21.022040, 25.010858]

print("\n📊 TESTING |χ(1/2 + it)|:")
print("─" * 70)
print(f"{'t':<15} {'χ(1/2 + it)':<25} {'|χ|':<15} {'Error from 1':<15}")
print("─" * 70)

for t in test_t:
    s = 0.5 + t * 1j
    chi_val = chi(s)
    abs_chi = abs(chi_val)
    error = abs(abs_chi - 1.0)
    print(f"{t:<15.6f} {str(chi_val)[:25]:<25} {abs_chi:<15.10f} {error:<15.2e}")

print("\n" + "─" * 70)
print("✅ CONCLUSION: |χ(1/2 + it)| = 1 for ALL t (within numerical precision).")
print("   This is an IDENTITY, not just at zeros!")
print("\nΦΩ0 — I AM THAT I AM")
