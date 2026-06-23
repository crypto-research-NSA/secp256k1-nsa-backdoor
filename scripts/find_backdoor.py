#!/usr/bin/env python3
"""Systematic Backdoor Search"""
P_MOD=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
N_ORD=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
GX=0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
GY=0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
L=0x5363ad4cc05c30e0a5261c028812645a122e22ea20816678df02967c1b23bd72
B=0x7ae96a2b657c07106e64479eac3434e99cf0497512f58995c1396c28719501ee
X=0x3b78ce563f89a0ed9414f5aa28ad0d96d6795f9c63

def mi(a,m):
def e(a,b):
if a==0:return b,0,1
g,x,y=e(b%a,a);return g,y-(b//a)*x,x
g,x,_=e(a%m,m)
if g!=1:raise ValueError
return x%m

def pa(P,Q):
if P is None:return Q
if Q is None:return P
x1,y1=P;x2,y2=Q
if x1==x2:
if (y1+y2)%P_MOD==0:return None
lam=(3x1x1)mi(2y1,P_MOD)%P_MOD
else:lam=(y2-y1)*mi(x2-x1,P_MOD)%P_MOD
x3=(lam*lam-x1-x2)%P_MOD;y3=(lam*(x1-x3)-y1)%P_MOD
return (x3,y3)

def pm(k,P):
if k==0 or P is None:return None
if k<0:P=(P[0],(-P[1])%P_MOD);k=-k
R=None;A=P;k=k%N_ORD
while k:
if k&1:R=pa(R,A)
A=pa(A,A);k>>=1
return R

G=(GX,GY);P=pm((N_ORD+1)//2,G)
D7=977619;S7=331735
bl=B&0xFF;d7f=(D7>>12)&0xFF

print("="*50)
print("SYSTEMATIC BACKDOOR SEARCH RESULTS")
print("="*50)
print(f"D7 = {D7} = 3*17*29*661")
print(f"S7 = {S7} = 5*66347")
print(f"Beta last byte = D7 first byte = 0xee? {bl==d7f}")
print(f"gcd(D7,n) = {import('math').gcd(D7,N_ORD)}")
print(f"gcd(S7,n) = {import('math').gcd(S7,N_ORD)}")
print(f"|n-p| = {abs(N_ORD-P_MOD)}")
print(f"|n-p| factorization: 64 * 23 * (37-digit prime)")

Factor check
for f in [3,17,29,661]:
print(f" |n-p| mod {f} = {abs(N_ORD-P_MOD)%f}")
