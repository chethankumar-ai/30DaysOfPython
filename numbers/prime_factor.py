def prime_factors(n):
    if n < 2:
        return []
    for i in range(2, n):
        if n % i == 0:
            return [i] + prime_factors(n // i)
    return [n]
print(list(set(prime_factors(100))))