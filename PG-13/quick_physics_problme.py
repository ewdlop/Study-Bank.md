import random

def velocity_problem():
    distance = random.randint(10, 500)  # Distance in meters
    time = random.randint(1, 10)  # Time in seconds
    velocity = distance / time
    problem = f"A car travels {distance} meters in {time} seconds. What is its velocity?"
    return problem, velocity

problem, solution = velocity_problem()
print(problem)
print(f"Answer: {solution:.2f} m/s")
