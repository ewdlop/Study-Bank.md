import random
import math
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to generate binary and hexadecimal problems and their solutions
def generate_problems_with_solutions(num_problems=10):
    problems = []
    solutions = []
    
    for _ in range(num_problems):
        bin1 = f"{random.randint(1, 255):08b}"
        bin2 = f"{random.randint(1, 255):08b}"
        hex1 = f"{random.randint(1, 255):02X}"
        hex2 = f"{random.randint(1, 255):02X}"
        shift_amount = random.randint(1, 4)
        
        # Addition and Multiplication in Binary
        bin_add = f"{bin1} + {bin2}"
        bin_mult = f"{bin1} * {bin2}"
        bin_add_sol = f"{int(bin1, 2) + int(bin2, 2):08b}"
        bin_mult_sol = f"{int(bin1, 2) * int(bin2, 2):08b}"
        
        # Addition and Multiplication in Hexadecimal
        hex_add = f"{hex1} + {hex2}"
        hex_mult = f"{hex1} * {hex2}"
        hex_add_sol = f"{int(hex1, 16) + int(hex2, 16):02X}"
        hex_mult_sol = f"{int(hex1, 16) * int(hex2, 16):02X}"
        
        # Conversion between Binary and Hexadecimal
        bin_to_hex = f"{bin1} to hexadecimal"
        hex_to_bin = f"{hex1} to binary"
        bin_to_hex_sol = f"{int(bin1, 2):02X}"
        hex_to_bin_sol = f"{int(hex1, 16):08b}"
        
        # Bitwise Operations
        bitwise_and = f"{bin1} AND {bin2}"
        bitwise_or = f"{bin1} OR {bin2}"
        bitwise_xor = f"{bin1} XOR {bin2}"
        bitwise_and_sol = f"{int(bin1, 2) & int(bin2, 2):08b}"
        bitwise_or_sol = f"{int(bin1, 2) | int(bin2, 2):08b}"
        bitwise_xor_sol = f"{int(bin1, 2) ^ int(bin2, 2):08b}"
        
        # Shift Operations
        left_shift = f"{bin1} << {shift_amount}"
        right_shift = f"{bin1} >> {shift_amount}"
        arithmetic_right_shift = f"{bin1} >>> {shift_amount}"
        left_shift_sol = f"{int(bin1, 2) << shift_amount:08b}"
        right_shift_sol = f"{int(bin1, 2) >> shift_amount:08b}"
        arithmetic_right_shift_sol = f"{(int(bin1, 2) >> shift_amount):08b}"
        
        # Base 2 and Base 16 Logarithms
        base2_log = f"log2({int(bin1, 2)})"
        base16_log = f"log16({int(bin1, 2)})"
        base2_log_sol = f"{math.log2(int(bin1, 2)):.2f}"
        base16_log_sol = f"{math.log(int(bin1, 2), 16):.2f}"
        
        problems.extend([bin_add, bin_mult, hex_add, hex_mult, bin_to_hex, hex_to_bin, bitwise_and, bitwise_or, bitwise_xor, left_shift, right_shift, arithmetic_right_shift, base2_log, base16_log])
        solutions.extend([bin_add_sol, bin_mult_sol, hex_add_sol, hex_mult_sol, bin_to_hex_sol, hex_to_bin_sol, bitwise_and_sol, bitwise_or_sol, bitwise_xor_sol, left_shift_sol, right_shift_sol, arithmetic_right_shift_sol, base2_log_sol, base16_log_sol])
    
    return problems, solutions

# Function to save problems and solutions to a PDF
def save_problems_and_solutions_to_pdf(problems, solutions, filename="binary_hex_problems_solutions.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    c.setFont("Helvetica", 12)
    y_position = height - 40
    
    c.drawString(40, y_position, "Binary and Hexadecimal Problems")
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
