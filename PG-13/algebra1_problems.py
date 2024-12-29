import random
from sympy import symbols, Eq, solve

def guess_purpose():
    print("Can you guess the purpose of the functions in this file?")

def generate_linear_equation():
    # Generate random coefficients for the linear equation
    x = symbols('x')
    a = random.randint(1, 10)
    b = random.randint(-10, 10)
    c = random.randint(1, 10)
    
    # Create the equation ax + b = c
    equation = Eq(a * x + b, c)
    solution = solve(equation, x)
    
    question = f"Solve the equation: {a}x + ({b}) = {c}"
    return question, solution[0]

def generate_quadratic_equation():
    # Generate random coefficients for the quadratic equation
    x = symbols('x')
    a = random.randint(1, 5)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    
    # Create the quadratic equation ax^2 + bx + c = 0
    equation = Eq(a * x**2 + b * x + c, 0)
    solutions = solve(equation, x)
    
    question = f"Solve the quadratic equation: {a}x^2 + ({b})x + ({c}) = 0"
    return question, solutions

def generate_inequality():
    # Generate random coefficients for the inequality
    x = symbols('x')
    a = random.randint(1, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    
    # Create the inequality ax + b > c
    inequality = a * x + b > c
    solution = solve(inequality, x)
    
    question = f"Solve the inequality: {a}x + ({b}) > {c}"
    return question, solution

def generate_expression_simplification():
    # Generate random terms for expression simplification
    x = symbols('x')
    a1 = random.randint(1, 10)
    b1 = random.randint(1, 10)
    a2 = random.randint(1, 10)
    b2 = random.randint(1, 10)
    
    expression = a1 * x + b1 - (a2 * x + b2)
    simplified_expression = expression.simplify()
    
    question = f"Simplify the expression: {a1}x + {b1} - ({a2}x + {b2})"
    return question, simplified_expression

def generate_algebra_question():
    # Randomly choose which type of question to generate
    question_type = random.choice(['linear', 'quadratic', 'inequality', 'simplification'])
    
    if question_type == 'linear':
        return generate_linear_equation()
    elif question_type == 'quadratic':
        return generate_quadratic_equation()
    elif question_type == 'inequality':
        return generate_inequality()
    elif question_type == 'simplification':
        return generate_expression_simplification()

# Generate a question
question, answer = generate_algebra_question()

# Output the question and answer
print("Algebra 1 Question:")
print(question)
print("Answer:")
print(answer)

guess_purpose()
