def f(x):
    return x * x  # Define your function here

def simpson(a, b, n):
    h = (b - a) / n
    sum1 = sum(f(a + i * h) for i in range(1, n, 2))
    sum2 = sum(f(a + i * h) for i in range(2, n - 1, 2))
    return (h / 3) * (f(a) + 4 * sum1 + 2 * sum2 + f(b))


# Example usage
a = 0  # Lower limit
b = 10  # Upper limit
n = 10  # Number of intervals (should be even)
result = simpson(a, b, n)
print("The integral is:", result)
