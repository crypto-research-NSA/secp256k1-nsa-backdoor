#!/usr/bin/env python3
"""Nibble Frequency Analysis"""
from collections import Counter
X=0x3b78ce563f89a0ed9414f5aa28ad0d96d6795f9c63
b=format(X,'0256b')
nibs=[b[i:i+4] for i in range(0,256,4)]
f=Counter(nibs)
print("="*50)
print("NIBBLE FREQUENCY ANALYSIS")
print("="*50)
print(f"Total nibbles: 64, Unique: {len(f)}")
print(f"Most common: '0000' ({f['0000']} times)")
print(f"Expected random: ~4 times")
print(f"Deviation: {f['0000']/4:.1f}x")
