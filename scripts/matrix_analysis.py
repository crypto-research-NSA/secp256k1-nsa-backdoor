#!/usr/bin/env python3
"""8x8 Nibble Matrix Analysis"""
X=0x3b78ce563f89a0ed9414f5aa28ad0d96d6795f9c63
b=format(X,'0256b')
print("="*50)
print("8x8 NIBBLE MATRIX OF x(G/2)")
print("="*50)
print("\nHex Matrix:")
for r in range(8):
row=[hex(int(b[r*32+c*4:r*32+c*4+4],2))[2:] for c in range(8)]
print(f"Row {r}: "+" ".join(row))
print("\nMain diagonal D7:",end=" ")
for i in range(8):print(hex(int(b[i*32+i*4:i*32+i*4+4],2))[2:],end=" ")
print(f"\nD7 = 0xeead3 = 977619 = 3*17*29*661")
BETA=0x7ae96a2b657c07106e64479eac3434e99cf0497512f58995c1396c28719501ee
print(f"\nBeta last byte: 0x{BETA&0xFF:02x}")
print(f"D7 first byte: 0x{(0xeead3>>12)&0xFF:02x}")
print(f"Match: {(BETA&0xFF)==((0xeead3>>12)&0xFF)}")
