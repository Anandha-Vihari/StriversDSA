import math

def simple_sieve(limit):
    is_prime=[True]*(limit+1)
    is_prime[0]=is_prime[1]=False

    for i in range(2,int(math.sqrt(limit))+1):
        if is_prime[i]:
            for j in range(i*i,limit+1,i):
                is_prime[j]=False

    primes=[]
    for i in range(2,limit+1):
        if is_prime[i]:
            primes.append(i)
    return primes

print(simple_sieve(10))

def segmented_sieve(M,N):
    if M<2:
        M=2
    limit=int(math.sqrt(N)+1)
    primes=simple_sieve(limit)

    size=N-M+1
    is_prime=[True]*size
    for prime in primes:
        first_multiple=(M//prime)*prime
        if first_multiple<M:
            first_multiple+=prime

        if first_multiple==prime:
            first_multiple+=prime

        for j in range(first_multiple,N+1,prime):
            is_prime[j-M]=False
























































