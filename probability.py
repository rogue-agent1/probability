#!/usr/bin/env python3
"""Probability distributions and statistical tests."""
import math,random
def normal_pdf(x,mu=0,sigma=1): return math.exp(-(x-mu)**2/(2*sigma**2))/(sigma*math.sqrt(2*math.pi))
def normal_cdf(x,mu=0,sigma=1): return 0.5*(1+math.erf((x-mu)/(sigma*math.sqrt(2))))
def binomial_pmf(k,n,p): return math.comb(n,k)*p**k*(1-p)**(n-k)
def poisson_pmf(k,lam): return lam**k*math.exp(-lam)/math.factorial(k)
def exponential_pdf(x,lam): return lam*math.exp(-lam*x) if x>=0 else 0
def chi_squared(observed,expected):
    stat=sum((o-e)**2/e for o,e in zip(observed,expected))
    df=len(observed)-1; return stat,df
def t_test(sample1,sample2):
    n1,n2=len(sample1),len(sample2)
    m1=sum(sample1)/n1;m2=sum(sample2)/n2
    v1=sum((x-m1)**2 for x in sample1)/(n1-1);v2=sum((x-m2)**2 for x in sample2)/(n2-1)
    se=math.sqrt(v1/n1+v2/n2);t=(m1-m2)/se if se>0 else 0
    df=n1+n2-2; return t,df
def sample_mean_ci(data,z=1.96):
    n=len(data);m=sum(data)/n;s=math.sqrt(sum((x-m)**2 for x in data)/(n-1))
    me=z*s/math.sqrt(n); return m-me,m,m+me
if __name__=="__main__":
    assert abs(normal_pdf(0)-0.3989)<0.001
    assert abs(normal_cdf(0)-0.5)<0.001
    assert abs(binomial_pmf(3,10,0.5)-0.1172)<0.001
    assert abs(poisson_pmf(3,2)-0.1804)<0.001
    random.seed(42);data=[random.gauss(100,15) for _ in range(100)]
    lo,m,hi=sample_mean_ci(data)
    print(f"Mean: {m:.2f}, 95% CI: [{lo:.2f}, {hi:.2f}]")
    print("Probability OK")
