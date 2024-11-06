import random

# Pattern Recognition (Number Sequence)
def generate_number_sequence():
    # Create a simple arithmetic progression (IQ test-style pattern)
    start = random.randint(1, 10)
    diff = random.randint(1, 5)
    length = 5
    
    sequence = [start + i * diff for i in range(length)]
    missing_index = random.randint(0, length - 1)
    
    # Hide one number in the sequence
    sequence_with_missing = sequence[:]
    sequence_with_missing[missing_index] = "?"
    
    question = f"Find the missing number in the sequence: {sequence_with_missing}"
    answer = sequence[missing_index]
    
    return question, answer

# Logical Deduction (Syllogism)
def generate_syllogism():
    subjects = ["All dogs", "Some cats", "No birds", "All humans"]
    predicates = ["are mammals", "are carnivores", "can fly", "have wings"]
    
    premise1 = random.choice(subjects) + " " + random.choice(predicates)
    premise2 = random.choice(subjects) + " " + random.choice(predicates)
    
    # Create a simple deductive reasoning puzzle
    question = f"Premise 1: {premise1}. \nPremise 2: {premise2}. \nWhat can be deduced from the two premises?"
    answer = "Answer will vary depending on the combination."
    
    return question, answer

# Verbal Reasoning (Analogies)
def generate_verbal_analogy():
    analogies = [
        ("Cat", "Kitten", "Dog", "Puppy"),
        ("Car", "Engine", "Body", "Heart"),
        ("Tree", "Leaf", "Book", "Page"),
        ("Sun", "Day", "Moon", "Night"),
    ]
    
    analogy = random.choice(analogies)
    question = f"{analogy[0]} is to {analogogy[1]} as {analogy[2]} is to ?"
    answer = analogy[3]
    
    return question, answer

# Math Puzzle (Arithmetic)
def generate_math_puzzle():
    operations = ['+', '-', '*', '/']
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    operation = random.choice(operations)
    
    if operation == '/':
        a = a * b  # Make sure the division results in an integer
    
    question = f"Solve: {a} {operation} {b}"
    if operation == '+':
        answer = a + b
    elif operation == '-':
        answer = a - b
    elif operation == '*':
        answer = a * b
    elif operation == '/':
        answer = a // b
    
    return question, answer

# Generate an IQ Test-style question
def generate_iq_test_question():
    question_type = random.choice(['number_sequence', 'syllogism', 'analogy', 'math_puzzle'])
    
    if question_type == 'number_sequence':
        return generate_number_sequence()
    elif question_type == 'syllogism':
        return generate_syllogism()
    elif question_type == 'analogy':
        return generate_verbal_analogy()
    elif question_type == 'math_puzzle':
        return generate_math_puzzle()

# Generate a question
question, answer = generate_iq_test_question()

# Display the generated question and answer
print("IQ Test Question:")
print(question)
print("Answer:")
print(answer)
