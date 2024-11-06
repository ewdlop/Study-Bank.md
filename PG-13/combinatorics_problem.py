import random
import math
from itertools import permutations, combinations

def factorial(n):
    return math.factorial(n)

def generate_permutation_problem():
    # Generate random values for n and r
    n = random.randint(4, 8)
    r = random.randint(2, n)
    
    # Calculate number of permutations
    perm = factorial(n) // factorial(n - r)
    
    # Create the problem description
    problem = f"How many ways can you arrange {r} items out of {n}?"
    return problem, perm

def generate_combination_problem():
    # Generate random values for n and r
    n = random.randint(5, 10)
    r = random.randint(2, n)
    
    # Calculate number of combinations
    comb = factorial(n) // (factorial(r) * factorial(n - r))
    
    # Create the problem description
    problem = f"How many ways can you choose {r} items from {n} distinct items?"
    return problem, comb

def generate_permutation_with_repetition():
    # Generate a random word with repeated letters
    letters = ['A', 'B', 'C', 'D']
    word = ''.join(random.choices(letters, k=6))
    
    # Count occurrences of each letter
    letter_count = {letter: word.count(letter) for letter in set(word)}
    
    # Calculate the number of permutations with repetition
    total_permutations = factorial(len(word))
    for count in letter_count.values():
        total_permutations //= factorial(count)
    
    # Create the problem description
    problem = f"How many ways can you arrange the word '{word}' considering repeated letters?"
    return problem, total_permutations

def generate_combination_with_replacement():
    # Generate random values for n and r
    n = random.randint(4, 7)
    r = random.randint(3, 6)
    
    # Calculate combinations with replacement
    comb_with_replacement = factorial(n + r - 1) // (factorial(r) * factorial(n - 1))
    
    # Create the problem description
    problem = f"How many ways can you choose {r} items from {n} distinct items with replacement?"
    return problem, comb_with_replacement

def generate_combinatorics_problem():
    problem_type = random.choice([
        'permutation', 
        'combination', 
        'permutation_with_repetition', 
        'combination_with_replacement'
    ])
    
    if problem_type == 'permutation':
        return generate_permutation_problem()
    elif problem_type == 'combination':
        return generate_combination_problem()
    elif problem_type == 'permutation_with_repetition':
        return generate_permutation_with_repetition()
    elif problem_type == 'combination_with_replacement':
        return generate_combination_with_replacement()

# Generate a random combinatorics problem
problem, answer = generate_combinatorics_problem()

# Output the problem and the solution
print("Combinatorics Problem:")
print(problem)
print("Answer:")
print(answer)
