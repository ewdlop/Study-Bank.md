# Study Bank

A collection of educational problem generators and solution management tools for various subjects including algebra, calculus, computer science, and more.

## Features

- **Problem Generators**: Automated problem generation for multiple subjects (see `PG-13/` directory)
- **Encrypted Solution Manual**: Secure storage and distribution of problem solutions with password-based encryption
- **Various Subjects**: Algebra, Calculus, Linear Algebra, Boolean Algebra, Computer Networks, and more

## Getting Started

### Problem Generators

The `PG-13` directory contains various problem generators for different subjects:

- `algebra1_problems.py` - Linear equations, quadratic equations, inequalities
- `calculus.py` - Derivatives, integrals, algebraic equations
- `linear_algebra.py` - Matrix operations, linear systems
- `generate_problems_with_solutions.py` - Binary and hexadecimal operations
- And many more...

### Encrypted Solution Manual

Securely manage solution manuals with password-based encryption. Perfect for teachers who want to distribute problems while keeping solutions secure.

**Quick Start:**

```bash
# Create an encrypted solution manual
python3 solution_manual_cli.py create -o my_solutions.enc

# View encrypted solutions (requires password)
python3 solution_manual_cli.py view my_solutions.enc --show-steps

# Verify password
python3 solution_manual_cli.py verify my_solutions.enc
```

For detailed documentation, see [ENCRYPTED_SOLUTION_MANUAL.md](ENCRYPTED_SOLUTION_MANUAL.md)

## Example: Generate Problems with Solutions

```python
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to generate arithmetic problems and their solutions
def generate_problems_with_solutions(num_problems=10):
    problems = []
    solutions = []
    operations = ['+', '-', '*', '/']
    
    for _ in range(num_problems):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operation = random.choice(operations)
        
        if operation == '/':
            num1 = num1 * num2  # Ensure division results in an integer
        
        problem = f"{num1} {operation} {num2}"
        solution = eval(problem)
        
        problems.append(problem)
        solutions.append(solution)
    
    return problems, solutions

# Function to save problems and solutions to a PDF
def save_problems_and_solutions_to_pdf(problems, solutions, filename="arithmetic_problems_solutions.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    c.setFont("Helvetica", 12)
    y_position = height - 40
    
    c.drawString(40, y_position, "Arithmetic Problems")
    y_position -= 20
    
    for i, problem in enumerate(problems):
        c.drawString(40, y_position, f"{i+1}. {problem} = ")
        y_position -= 20
        
        if y_position < 40:  # Start new page if space is insufficient
            c.showPage()
            c.setFont("Helvetica", 12)
            y_position = height - 40
    
    c.showPage()
    y_position = height - 40
    c.drawString(40, y_position, "Solutions")
    y_position -= 20
    
    for i, solution in enumerate(solutions):
        c.drawString(40, y_position, f"{i+1}. {solution}")
        y_position -= 20
        
        if y_position < 40:  # Start new page if space is insufficient
            c.showPage()
            c.setFont("Helvetica", 12)
            y_position = height - 40
    
    c.save()

# Generate and save problems with solutions
problems, solutions = generate_problems_with_solutions(num_problems=30)
save_problems_and_solutions_to_pdf(problems, solutions)
```

## Installation

Requirements:
- Python 3.7+
- cryptography library (for encrypted solution manuals)
- reportlab (for PDF generation)
- sympy (for symbolic mathematics)

```bash
pip install cryptography reportlab sympy
```

## Security

See [SECURITY.md](SECURITY.md) for security policies and vulnerability reporting.

For encrypted solution manuals, please follow the security best practices outlined in [ENCRYPTED_SOLUTION_MANUAL.md](ENCRYPTED_SOLUTION_MANUAL.md).

## License

See [LICENSE](LICENSE) for license information.

