def time(func):
    def inner(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Total time taken: {end - start:.6f} seconds")
        return result
    return inner

@time
def factorial(n):
    def inner_fact(x):  # inner function does actual recursion
        if x == 0 or x == 1:
            return 1
        return x * inner_fact(x - 1)
    
    return inner_fact(n)  # only outer call is timed
print(factorial(5))
