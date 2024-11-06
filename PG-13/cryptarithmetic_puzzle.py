import random

def generate_cryptarithmetic():
    letters = "SEND MORE MONEY"
    mapping = {ch: random.randint(0, 9) for ch in set(letters) if ch != ' '}
    problem = "SEND + MORE = MONEY"
    return problem, mapping

problem, mapping = generate_cryptarithmetic()
print(f"Problem: {problem}")
print(f"Letter Mapping: {mapping}")
Yeah
