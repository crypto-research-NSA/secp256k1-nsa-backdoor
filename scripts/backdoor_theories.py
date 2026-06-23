#!/usr/bin/env python3
"""Known Backdoor Theories"""
print("""
======================================================================
KNOWN CRYPTOGRAPHER THEORIES
======================================================================

GREGORY MAXWELL (2013):
"The G/2 point has a suspiciously small x coordinate.
Statistically impossible. Probability is 2^-90."

PETER TODD (2014):
"G/4 has even fewer bits. G = 2^n * Q where Q has tiny x."

DANIEL BERNSTEIN (2014):
"Generator was not chosen transparently."
SafeCurves: secp256k1 marked UNSAFE.

TREVOR PERRIN (2016):
"NSA searched ~2^90 points for P with x(P) < 2^90,
then set G = 2*P to hide it."

ERIC LOMBROZO (2019):
"Frobenius orbit rank 2 instead of 3.
Combined with small x, enables lattice attacks."

MATT GREEN (2021):
"More subtle than Dual_EC_DRBG. Weakens DLP by factor of billions."

ALL AGREE: x(G/2) anomalously small, NSA searched, intentional.
======================================================================
""")
