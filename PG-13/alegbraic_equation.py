from sympy import symbols, Eq, solve
x = symbols('x')
equation = Eq(2*x + 5, 15)
solution = solve(equation)
print(solution)
