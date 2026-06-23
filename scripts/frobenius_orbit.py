#!/usr/bin/env python3
"""Frobenius Orbit Verification"""
P_MOD=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
N_ORD=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
GX=0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
GY=0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
L=0x5363ad4cc05c30e0a5261c028812645a122e22ea20816678df02967c1b23bd72
B=0x7ae96a2b657c07106e64479eac3434e99cf0497512f58995c1396c28719501ee

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

G=(GX,GY);P0=pm((N_ORD+1)//2,G)
P1=pm(L,P0);P2=pm((L*L)%N_ORD,P0)
orb=pa(pa(P0,P1),P2)

print("="*50)
print("FROBENIUS ORBIT VERIFICATION")
print("="*50)
print(f"P0+P1+P2 = O? {orb is None}")
print(f"lambda*P0 = P1? {pm(L,P0)[0]==P1[0]}")
print(f"lambda*P1 = P2? {pm(L,P1)[0]==P2[0]}")
print(f"y(P0)=y(P1)=y(P2)? {P0[1]==P1[1]==P2[1]}")
print(f"x(P1)=betax(P0)? {(BP0[0])%P_MOD==P1[0]}")
