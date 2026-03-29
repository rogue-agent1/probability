#!/usr/bin/env python3
"""probability - Probability distributions and sampling."""
import sys, math, random

def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

def comb(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

def binomial_pmf(k, n, p):
    return comb(n, k) * p**k * (1-p)**(n-k)

def binomial_cdf(k, n, p):
    return sum(binomial_pmf(i, n, p) for i in range(k + 1))

def poisson_pmf(k, lam):
    return math.exp(-lam) * lam**k / factorial(k)

def normal_pdf(x, mu=0, sigma=1):
    return math.exp(-0.5*((x-mu)/sigma)**2) / (sigma * math.sqrt(2*math.pi))

def normal_cdf(x, mu=0, sigma=1):
    return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))

def exponential_pdf(x, lam):
    return lam * math.exp(-lam * x) if x >= 0 else 0

def sample_normal(mu=0, sigma=1):
    u1 = random.random()
    u2 = random.random()
    z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    return mu + sigma * z

def test():
    # binomial: coin flip
    assert abs(binomial_pmf(5, 10, 0.5) - 0.24609375) < 1e-6
    assert abs(binomial_cdf(10, 10, 0.5) - 1.0) < 1e-9
    # poisson
    assert abs(poisson_pmf(0, 1) - math.exp(-1)) < 1e-9
    assert abs(sum(poisson_pmf(k, 3) for k in range(20)) - 1.0) < 1e-6
    # normal
    assert abs(normal_cdf(0) - 0.5) < 1e-9
    assert abs(normal_cdf(1.96) - 0.975) < 0.001
    assert abs(normal_pdf(0) - 1/math.sqrt(2*math.pi)) < 1e-9
    # sampling
    random.seed(42)
    samples = [sample_normal(10, 2) for _ in range(10000)]
    mean = sum(samples) / len(samples)
    assert abs(mean - 10) < 0.1
    print("OK: probability")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        print("Usage: probability.py test")
