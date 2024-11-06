from z3 import *

# Define two integer variables
x = Int('x')
y = Int('y')

# Create a solver
s = Solver()

# Add some constraints
s.add(x + y > 10, x > 0, y > 0)

# Check satisfiability
if s.check() == sat:
    print("Solution: ", s.model())
else:
    print("No solution")
