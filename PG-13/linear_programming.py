from pulp import LpMaximize, LpProblem, LpVariable

# Define the problem
prob = LpProblem("ExampleProblem", LpMaximize)

# Create decision variables
x = LpVariable("x", lowBound=0, upBound=10, cat='Integer')
y = LpVariable("y", lowBound=0, upBound=10, cat='Integer')

# Define the objective function
prob += x + y

# Define the constraints
prob += 2 * x + 3 * y <= 12
prob += -x + y >= 3

# Solve the problem
prob.solve()

# Output the result
print("Optimal values for x and y:")
print("x =", x.varValue)
print("y =", y.varValue)
