import math

def simple_sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    
    primes = []
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
    return primes

def segmented_sieve(M, N):
    if M < 2:
        M = 2
    
    # Get primes up to sqrt(N)
    limit = int(math.sqrt(N)) + 1
    primes = simple_sieve(limit)
    
    # Create array for range [M, N]
    size = N - M + 1
    is_prime = [True] * size
    
    # Mark multiples of each prime
    for prime in primes:
        # Find first multiple >= M
        first_multiple = (M // prime) * prime
        if first_multiple < M:
            first_multiple += prime
        
        # Don't mark the prime itself
        if first_multiple == prime:
            first_multiple += prime
        
        # Mark all multiples in range
        for j in range(first_multiple, N + 1, prime):
            is_prime[j - M] = False
    
    # Collect primes
    result = []
    for i in range(size):
        if is_prime[i]:
            result.append(M + i)
    return result

# Main code for your problem
t = int(input())
for _ in range(t):
    M, N = map(int, input().split())
    primes = segmented_sieve(M, N)
    for p in primes:
        print(p)
    print()  # Extra newline between test cases






































