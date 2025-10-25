# Encrypted Solution Manual

This system provides secure encryption and decryption of solution manuals for educational purposes. It allows teachers and educators to distribute problem sets while keeping solutions encrypted and accessible only with the correct password.

## Features

- **Password-based encryption**: Solutions are encrypted using strong AES-256 encryption via Fernet symmetric encryption
- **Key derivation**: Uses PBKDF2-HMAC-SHA256 with 100,000 iterations for secure key generation from passwords
- **Easy-to-use CLI**: Command-line interface for creating, viewing, and managing encrypted solution manuals
- **Flexible format**: Supports structured JSON format for organizing problems by subject
- **Sample data included**: Can generate sample solution manuals for testing

## Installation

The system requires Python 3.7+ and the `cryptography` library:

```bash
pip install cryptography
```

## Quick Start

### Create an Encrypted Solution Manual

Create a new encrypted solution manual with sample data:

```bash
python3 solution_manual_cli.py create -o my_solutions.enc -p YourSecurePassword
```

### View Solutions

View the encrypted solutions (requires password):

```bash
python3 solution_manual_cli.py view my_solutions.enc -p YourSecurePassword --show-steps
```

### Verify Password

Check if a password is correct without viewing the solutions:

```bash
python3 solution_manual_cli.py verify my_solutions.enc -p YourSecurePassword
```

### Export to JSON

Export the encrypted solutions to a plain JSON file (for backup or editing):

```bash
python3 solution_manual_cli.py export my_solutions.enc -o solutions.json -p YourSecurePassword
```

## Usage Guide

### Command-Line Interface

The CLI provides four main commands:

#### 1. Create Command

Create a new encrypted solution manual:

```bash
python3 solution_manual_cli.py create [OPTIONS]

Options:
  -i, --input FILE      Input JSON file with solution data (optional)
  -o, --output FILE     Output encrypted file (default: encrypted_solutions.dat)
  -p, --password PASS   Encryption password (will prompt if not provided)
```

**Examples:**

```bash
# Create with sample data (will prompt for password)
python3 solution_manual_cli.py create -o solutions.enc

# Create from existing JSON file
python3 solution_manual_cli.py create -i my_solutions.json -o solutions.enc -p MyPassword

# Create with password on command line (less secure, but convenient for scripts)
python3 solution_manual_cli.py create -o solutions.enc -p SecurePassword123
```

#### 2. View Command

View an encrypted solution manual:

```bash
python3 solution_manual_cli.py view FILE [OPTIONS]

Options:
  -p, --password PASS   Decryption password (will prompt if not provided)
  --show-steps          Show solution steps
  --format FORMAT       Output format: 'text' or 'json' (default: text)
```

**Examples:**

```bash
# View with interactive password prompt
python3 solution_manual_cli.py view solutions.enc

# View with solution steps
python3 solution_manual_cli.py view solutions.enc -p MyPassword --show-steps

# Output as JSON
python3 solution_manual_cli.py view solutions.enc -p MyPassword --format json
```

#### 3. Export Command

Export encrypted solutions to plain JSON:

```bash
python3 solution_manual_cli.py export FILE -o OUTPUT [OPTIONS]

Options:
  -o, --output FILE     Output JSON file (required)
  -p, --password PASS   Decryption password (will prompt if not provided)
```

**Examples:**

```bash
# Export to JSON
python3 solution_manual_cli.py export solutions.enc -o plain_solutions.json -p MyPassword
```

#### 4. Verify Command

Verify that a password is correct:

```bash
python3 solution_manual_cli.py verify FILE [OPTIONS]

Options:
  -p, --password PASS   Password to verify (will prompt if not provided)
```

**Examples:**

```bash
# Verify with interactive password prompt
python3 solution_manual_cli.py verify solutions.enc

# Verify with password on command line
python3 solution_manual_cli.py verify solutions.enc -p MyPassword
```

### Python API

You can also use the encryption system directly in Python code:

```python
from encrypted_solution_manager import EncryptedSolutionManager

# Create manager
manager = EncryptedSolutionManager()

# Prepare solution data
solution_data = {
    "title": "My Solution Manual",
    "version": "1.0",
    "subjects": {
        "math": {
            "problems": [
                {
                    "id": "math_001",
                    "question": "What is 2 + 2?",
                    "solution": "4",
                    "steps": ["2 + 2 = 4"]
                }
            ]
        }
    }
}

# Encrypt and save
manager.save_encrypted_solution(
    solution_data,
    password="my_secure_password",
    filepath="solutions.enc"
)

# Load and decrypt
loaded_data = manager.load_encrypted_solution(
    filepath="solutions.enc",
    password="my_secure_password"
)

print(loaded_data)
```

## Solution Manual Format

Solution manuals use a structured JSON format:

```json
{
  "title": "Solution Manual Title",
  "version": "1.0",
  "subjects": {
    "subject_name": {
      "problems": [
        {
          "id": "unique_problem_id",
          "question": "The problem statement",
          "solution": "The final answer",
          "steps": [
            "Step 1 explanation",
            "Step 2 explanation",
            "Step 3 explanation"
          ]
        }
      ]
    }
  },
  "notes": "Additional notes or instructions"
}
```

### Example Solution Manual

```json
{
  "title": "Algebra 1 Solutions",
  "version": "1.0",
  "subjects": {
    "linear_equations": {
      "problems": [
        {
          "id": "lin_001",
          "question": "Solve for x: 3x + 7 = 22",
          "solution": "x = 5",
          "steps": [
            "3x + 7 = 22",
            "3x = 22 - 7",
            "3x = 15",
            "x = 5"
          ]
        }
      ]
    },
    "quadratic_equations": {
      "problems": [
        {
          "id": "quad_001",
          "question": "Solve: x^2 - 6x + 8 = 0",
          "solution": "x = 2 or x = 4",
          "steps": [
            "x^2 - 6x + 8 = 0",
            "(x - 2)(x - 4) = 0",
            "x = 2 or x = 4"
          ]
        }
      ]
    }
  },
  "notes": "These solutions are for teacher reference only."
}
```

## Security Considerations

### Password Strength

- Use strong passwords with at least 12 characters
- Include uppercase, lowercase, numbers, and special characters
- Avoid common words or easily guessable patterns
- Example: `T3@ch3r$P@ssw0rd!2025`

### Best Practices

1. **Never share encrypted files with the password**: Distribute encrypted files and passwords through separate channels
2. **Use different passwords**: Use different passwords for different solution manuals
3. **Secure storage**: Store encrypted files in secure locations with appropriate access controls
4. **Regular updates**: Change passwords periodically, especially if there's a risk of compromise
5. **Backup**: Keep encrypted backups of solution manuals in case of file corruption

### Technical Details

- **Encryption**: Fernet (AES-128-CBC with HMAC-SHA256 for authentication)
- **Key Derivation**: PBKDF2-HMAC-SHA256 with 100,000 iterations
- **Salt**: Uses a default salt (in production, should be randomly generated per file)
- **Password Security**: Passwords are never stored; only derived keys are used

## Use Cases

### For Teachers

1. **Distribute Problem Sets**: Share problem sets with students while keeping solutions encrypted
2. **Exam Preparation**: Create encrypted answer keys for exams
3. **Homework Solutions**: Provide encrypted solutions that can be revealed after due dates
4. **Tutoring**: Share solutions securely with tutors or teaching assistants

### For Students

1. **Self-Study**: Access solutions after attempting problems (with teacher-provided password)
2. **Verification**: Check work against encrypted solutions when allowed

### For Institutions

1. **Secure Archives**: Maintain secure archives of exam solutions
2. **Access Control**: Grant access to authorized personnel only
3. **Content Protection**: Prevent unauthorized distribution of solutions

## Troubleshooting

### Common Issues

**"Decryption failed" error**
- Check that you're using the correct password
- Verify that the encrypted file hasn't been corrupted
- Ensure you're using the same version of the encryption tool

**"Module not found" error**
- Install the cryptography library: `pip install cryptography`
- Verify Python version is 3.7 or higher

**Password prompt doesn't appear**
- If running in a non-interactive environment, use the `-p` option to provide password on command line

## Integration with Study Bank

This encrypted solution manual system integrates seamlessly with the Study Bank problem generators in the `PG-13` directory. You can:

1. Generate problems using the existing problem generators
2. Create a JSON file with problems and solutions
3. Encrypt the solution manual using this tool
4. Distribute problems to students and keep the encrypted solutions secure

## License

This encrypted solution manual system is part of the Study Bank project and follows the same license terms.

## Support

For issues, questions, or contributions, please refer to the main Study Bank repository.
