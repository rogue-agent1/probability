#!/usr/bin/env python3
"""Probability — combinatorics, distributions, Bayes theorem."""
import sys, math
def factorial(n):
    r=1
    for i in range(2,n+1): r*=i
    return r
def comb(n,r): return factorial(n)//(factorial(r)*factorial(n-r)) if r<=n else 0
def perm(n,r): return factorial(n)//factorial(n-r) if r<=n else 0
def binomial(n,k,p): return comb(n,k)*(p**k)*((1-p)**(n-k))
def poisson(k,lam): return (lam**k)*math.exp(-lam)/factorial(k)
def bayes(p_a, p_b_given_a, p_b): return p_a*p_b_given_a/p_b if p_b else 0
def cli():
    if len(sys.argv)<2: print("Usage: probability comb|perm|binom|poisson|bayes [args]"); sys.exit(1)
    cmd=sys.argv[1]
    if cmd=="comb": print(f"  C({sys.argv[2]},{sys.argv[3]}) = {comb(int(sys.argv[2]),int(sys.argv[3]))}")
    elif cmd=="perm": print(f"  P({sys.argv[2]},{sys.argv[3]}) = {perm(int(sys.argv[2]),int(sys.argv[3]))}")
    elif cmd=="binom":
        n,k,p=int(sys.argv[2]),int(sys.argv[3]),float(sys.argv[4])
        print(f"  B({n},{k},{p}) = {binomial(n,k,p):.6f}")
    elif cmd=="poisson":
        k,lam=int(sys.argv[2]),float(sys.argv[3])
        print(f"  P({k};λ={lam}) = {poisson(k,lam):.6f}")
    elif cmd=="bayes":
        pa,pba,pb=float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4])
        print(f"  P(A|B) = {bayes(pa,pba,pb):.6f}")
if __name__=="__main__": cli()
