from z3 import *

def generate_logic_puzzle():
    # Create boolean variables
    A, B, C, D = Bools('A B C D')
    
    # Define a complex solution (this will be the basis of the puzzle)
    solution = And(Or(A, Not(B)), Or(B, Not(C)), And(C, D), Not(A))
    
    # The puzzle asks which of the following variables can be True or False to satisfy the solution
    puzzle = Solver()
    puzzle.add(solution)
    
    # Get a model that satisfies the constraints (this is the answer)
    if puzzle.check() == sat:
        model = puzzle.model()
        # Reverse engineer: print a puzzle that leads to this solution
        print("To satisfy the following conditions, which of the variables A, B, C, D are True/False?")
        print("1. Either A is True or B is False.")
        print("2. Either B is True or C is False.")
        print("3. Both C and D are True.")
        print("4. A is False.")
        
        # Provide a model answer
        print("Answer: ")
        for v in [A, B, C, D]:
            print(f"{v}: {model[v]}")
    else:
        print("No solution found")

generate_logic_puzzle()
