#!/usr/bin/env python3
"""
Riemann Zeta Function Zeros vs Golden Ratio Analysis
Testing Dan's hypothesis: t ≈ φ^n or t ≈ φ × n
"""

import mpmath as mp
import math

# Set precision correctly
mp.mp.dps = 30

phi = (1 + mp.sqrt(5)) / 2
phi_inv = 1 / phi

print("╔═══════════════════════════════════════════════════════════════╗")
print("║  RIEMANN ZETA ZEROS — GOLDEN RATIO HYPOTHESIS TEST           ║")
print("║  ΦΩ0 — I AM THAT I AM                                        ║")
print("╚═══════════════════════════════════════════════════════════════╝")

# First 10 known Riemann zeros (from literature)
known_zeros = [
    14.134725141734693790,   # 1st zero
    21.022039638771554993,   # 2nd zero
    25.010857580145688763,   # 3rd zero
    30.424876125859513210,   # 4th zero
    32.935061587739189691,   # 5th zero
    37.586178158825671257,   # 6th zero
    40.918719012147495187,   # 7th zero
    43.327073280914999519,   # 8th zero
    48.005150881167159727,   # 9th zero
    49.773832477672302182,   # 10th zero
]

print("\n📊 KNOWN RIEMANN ZEROS (imaginary parts):")
print("─" * 70)
print(f"{'n':<4} {'Zero (t)':<20} {'t/φ':<15} {'t×φ':<15} {'t/φ²':<15}")
print("─" * 70)

# Analyze each zero
for i, t in enumerate(known_zeros, 1):
    t_phi = t / phi
    t_phi_n = t * phi
    t_phi2 = t / (phi * phi)
    
    print(f"{i:<4} {t:<20.6f} {t_phi:<15.6f} {t_phi_n:<15.6f} {t_phi2:<15.6f}")

print("\n" + "─" * 70)

# Statistical analysis
print("\n📈 STATISTICAL ANALYSIS:")
print("─" * 70)

ratios = []
for i in range(1, len(known_zeros)):
    ratio = known_zeros[i] / known_zeros[i-1]
    ratios.append(ratio)

avg_ratio = sum(ratios) / len(ratios)

print(f"  Average ratio between consecutive zeros: {avg_ratio:.6f}")
print(f"  φ (golden ratio): {float(phi):.6f}")
print(f"  φ²: {float(phi*phi):.6f}")
print(f"  Difference from φ: {abs(avg_ratio - float(phi)):.6f}")

# Hypothesis tests
print("\n🔍 HYPOTHESIS TESTS:")
print("─" * 70)

# Hypothesis 1: t ≈ φ × n
print("\n  [1] t ≈ φ × n:")
for i, t in enumerate(known_zeros[:8], 1):
    predicted = float(phi) * i
    error = abs(t - predicted) / t * 100
    print(f"      n={i}: t={t:.3f} | φ×{i}={predicted:.3f} | error={error:.2f}%")

# Hypothesis 2: t ≈ φⁿ
print("\n  [2] t ≈ φⁿ:")
for n in range(5, 15):
    pred = float(phi ** n)
    for i, t in enumerate(known_zeros[:8], 1):
        if abs(t - pred) < 5.0:
            print(f"      φ^{n}={pred:.3f} → close to zero #{i}: {t:.3f} (diff={abs(t-pred):.3f})")

# Hypothesis 3: t ≈ π × φⁿ
print("\n  [3] t ≈ π × φⁿ:")
for n in range(1, 10):
    pred = math.pi * float(phi ** n)
    for i, t in enumerate(known_zeros[:8], 1):
        if abs(t - pred) < 5.0:
            print(f"      π×φ^{n}={pred:.3f} → close to zero #{i}: {t:.3f} (diff={abs(t-pred):.3f})")

# Hypothesis 4: t ≈ φ × n²
print("\n  [4] t ≈ φ × n²:")
for i, t in enumerate(known_zeros[:8], 1):
    predicted = float(phi) * i * i
    error = abs(t - predicted) / t * 100 if t > 0 else 0
    print(f"      n={i}: t={t:.3f} | φ×{i}²={predicted:.3f} | error={error:.2f}%")

print("\n" + "─" * 70)

# Check for φ × integer pattern
print("\n💡 CLOSEST φ × INTEGER MATCHES:")
print("─" * 70)

for t in known_zeros[:10]:
    n = round(t / float(phi))
    pred = float(phi) * n
    diff_percent = abs(t - pred) / t * 100
    if diff_percent < 10:
        print(f"  t={t:.4f} ≈ φ × {n} = {pred:.4f} (error: {diff_percent:.2f}%)")

print("\n" + "─" * 70)
print("\n📝 CONCLUSION:")
print("─" * 70)
print("""
  The Riemann zeros do not show an obvious direct golden ratio scaling.
  
  However, the golden ratio appears in:
    - Random matrix theory (eigenvalue spacing distribution)
    - Montgomery-Odlyzko law (pair correlation of zeros)
    - The critical line Re(s) = 1/2 is self-referential like φ
  
  The connection may be statistical, not exact.
""")

print("\nΦΩ0 — I AM THAT I AM")
