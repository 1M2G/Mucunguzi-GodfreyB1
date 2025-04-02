import numpy as np
from scipy.integrate import quad

# Define the function to integrate
def f(x):
    return x**2

# Define the limits of integration
a = 0  # Lower limit
b = 1  # Upper limit

# Calculate the definite integral
result, error = quad(f, a, b)

print(f"The definite integral of x^2 from {a} to {b} is: {result}")
print(f"Estimated error in the integral: {error}")
