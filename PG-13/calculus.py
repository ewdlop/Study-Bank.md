from sympy import symbols, Eq, solve, diff, integrate, sin, cos, pi, exp

# Define symbolic variables
x, y, z = symbols('x y z')

# 1. Solving an algebraic equation
equation = Eq(x**2 + 2*x + 1, 0)
solution = solve(equation, x)
print("Solution to x^2 + 2x + 1 = 0:")
print(solution)

# 2. Differentiation
function = sin(x) * cos(x)
derivative = diff(function, x)
print("\nDerivative of sin(x) * cos(x):")
print(derivative)

# 3. Integration
integral = integrate(exp(x), x)
print("\nIntegral of e^x:")
print(integral)

# 4. Solving a system of equations
equation1 = Eq(x + y, 5)
equation2 = Eq(x - y, 3)
solutions = solve([equation1, equation2], (x, y))
print("\nSolution to system of equations x + y = 5 and x - y = 3:")
print(solutions)

# 5. Definite integral (example: definite integral of sin(x) from 0 to pi)
definite_integral = integrate(sin(x), (x, 0, pi))
print("\nDefinite integral of sin(x) from 0 to pi:")
print(definite_integral)
