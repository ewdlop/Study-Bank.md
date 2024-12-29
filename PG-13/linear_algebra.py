import numpy as np

def guess_purpose():
    print("Can you guess the purpose of the matrix puzzle?")

def generate_matrix_puzzle():
    # Create a random 2x2 matrix
    matrix = np.random.randint(1, 10, (2, 2))
    
    # Create a question about calculating the determinant of the matrix
    determinant = np.linalg.det(matrix)
    
    # Generate the question
    question = f"Given the matrix:\n{matrix}\nCalculate the determinant of the matrix."
    
    # The answer is the determinant
    answer = determinant
    
    print("Linear Algebra Puzzle:")
    print(question)
    print(f"Answer: {answer}")

generate_matrix_puzzle()
guess_purpose()
