# Function to dynamically include units in both the problem and solution
def generate_time_dilation_problem_with_units(value):
    velocity_percent = random.randint(50, 99)  # Percentage of the speed of light
    earth_time_years = random.randint(1, 100)  # Time on Earth in years
    velocity = (velocity_percent / 100) * c
    # Calculate astronaut's time using time dilation formula
    gamma = lorentz_factor(velocity)
    astronaut_time = earth_time_years / gamma
    problem = (f"A {value} travels at {velocity_percent}% the speed of light for {earth_time_years} years "
               "as measured from Earth. How much time does the astronaut aboard the {value} experience (in years)?")
    return problem, f"{astronaut_time:.2f} years"

def generate_length_contraction_problem_with_units(value):
    velocity_percent = random.randint(50, 99)  # Percentage of the speed of light
    rest_length = random.randint(10, 1000)  # Rest length in meters
    velocity = (velocity_percent / 100) * c
    # Calculate contracted length using length contraction formula
    gamma = lorentz_factor(velocity)
    contracted_length = rest_length / gamma
    problem = (f"A {value} is moving at {velocity_percent}% the speed of light. "
               f"The rest length of the {value} is {rest_length} meters. "
               "What is the contracted length of the {value} (in meters) as observed from a stationary observer?")
    return problem, f"{contracted_length:.2f} meters"

def generate_simultaneity_problem_with_units(value):
    velocity_percent = random.randint(50, 99)  # Percentage of the speed of light
    distance = random.randint(100, 1000)  # Distance in meters
    velocity = (velocity_percent / 100) * c
    # Calculate the time difference due to simultaneity
    time_difference = (velocity * distance) / c**2
    problem = (f"Two events occur {distance} meters apart on a {value} moving at {velocity_percent}% the speed of light. "
               "From the station's perspective, both events occur simultaneously. "
               "How much time passes between the events for an observer on the {value} (in microseconds)?")
    return problem, f"{time_difference * 1e6:.2f} microseconds"  # Convert seconds to microseconds

# Generate random problems with solutions and units
generated_time_dilation_problem_with_units = (
    Pipe("rocket")
    .pipe(generate_time_dilation_problem_with_units)
    .result()
)

generated_length_contraction_problem_with_units = (
    Pipe("rocket")
    .pipe(generate_length_contraction_problem_with_units)
    .result()
)

generated_simultaneity_problem_with_units = (
    Pipe("rocket")
    .pipe(generate_simultaneity_problem_with_units)
    .result()
)

generated_time_dilation_problem_with_units, generated_length_contraction_problem_with_units, generated_simultaneity_problem_with_units
