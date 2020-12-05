# project euler problem #2
# find largest prime factor of 600851475143

number = 600851475143

# going to need a sieve or something
# just do eratosthenes, but maybe revisit and do SQUFOF at some point?
def sieve(n):

    numbers = list(range(0, n + 1))
    for prime in numbers:

        if prime < 2:
            continue
        elif prime > (n ** 0.5):
            break
        for j in range(prime ** 2, n, prime):
            numbers[j] = 0

    return [i for i in numbers if i > 1]

# sieve for prime factors of number
print(max([fac for fac in sieve(number) if number % fac == 0]))