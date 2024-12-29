def guess_purpose():
    print("Can you guess the purpose of the functions in this file?")

def add_binary(bin1, bin2):
    # Convert binary strings to integers, add them, and convert back to binary
    result = bin(int(bin1, 2) + int(bin2, 2))
    return result[2:]  # Remove the '0b' prefix

def multiply_binary(bin1, bin2):
    # Convert binary strings to integers, multiply them, and convert back to binary
    result = bin(int(bin1, 2) * int(bin2, 2))
    return result[2:]  # Remove the '0b' prefix

def add_hex(hex1, hex2):
    # Convert hexadecimal strings to integers, add them, and convert back to hexadecimal
    result = hex(int(hex1, 16) + int(hex2, 16))
    return result[2:]  # Remove the '0x' prefix

def multiply_hex(hex1, hex2):
    # Convert hexadecimal strings to integers, multiply them, and convert back to hexadecimal
    result = hex(int(hex1, 16) * int(hex2, 16))
    return result[2:]  # Remove the '0x' prefix

def bin_to_hex(bin_str):
    # Convert binary string to hexadecimal string
    result = hex(int(bin_str, 2))
    return result[2:]  # Remove the '0x' prefix

def hex_to_bin(hex_str):
    # Convert hexadecimal string to binary string
    result = bin(int(hex_str, 16))
    return result[2:]  # Remove the '0b' prefix

def bitwise_and(bin1, bin2):
    # Perform bitwise AND operation on binary strings
    result = bin(int(bin1, 2) & int(bin2, 2))
    return result[2:]  # Remove the '0b' prefix

def bitwise_or(bin1, bin2):
    # Perform bitwise OR operation on binary strings
    result = bin(int(bin1, 2) | int(bin2, 2))
    return result[2:]  # Remove the '0b' prefix

def bitwise_xor(bin1, bin2):
    # Perform bitwise XOR operation on binary strings
    result = bin(int(bin1, 2) ^ int(bin2, 2))
    return result[2:]  # Remove the '0b' prefix

# Example usage
bin1 = "1010"  # Binary for 10
bin2 = "1100"  # Binary for 12

hex1 = "A"  # Hexadecimal for 10
hex2 = "C"  # Hexadecimal for 12

print(f"Addition of {bin1} and {bin2} in binary: {add_binary(bin1, bin2)}")
print(f"Multiplication of {bin1} and {bin2} in binary: {multiply_binary(bin1, bin2)}")

print(f"Addition of {hex1} and {hex2} in hexadecimal: {add_hex(hex1, hex2)}")
print(f"Multiplication of {hex1} and {hex2} in hexadecimal: {multiply_hex(hex1, hex2)}")

print(f"Binary {bin1} to hexadecimal: {bin_to_hex(bin1)}")
print(f"Hexadecimal {hex1} to binary: {hex_to_bin(hex1)}")

print(f"Bitwise AND of {bin1} and {bin2}: {bitwise_and(bin1, bin2)}")
print(f"Bitwise OR of {bin1} and {bin2}: {bitwise_or(bin1, bin2)}")
print(f"Bitwise XOR of {bin1} and {bin2}: {bitwise_xor(bin1, bin2)}")

guess_purpose()
